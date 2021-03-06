from eve import Eve
from flask import jsonify, request, url_for, redirect, flash
from flask_github import GitHub
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

import pymongo as pm

import requests
import json

from scanner import *
from log_script import create_logger
import config
assert db is not None

app = Eve()
app.config['GITHUB_CLIENT_ID'] = config.client_id
app.config['GITHUB_CLIENT_SECRET'] = config.client_secret
app.config['SECRET_KEY'] = config.secret_key

app.config["APPLICATION_ROOT"] = "/api"

github = GitHub(app)



@app.route('/scan/<git_username>')
def launch_scan(git_username):
    result = check_token(git_username)

    json_res = json.loads(result.get_data())
    if json_res['response'] == 500:
        return jsonify({"response": 500})

    apilogger = create_logger()
    if not manual_scan(git_username):
        apilogger.error("Manual scan failed")
        return jsonify({"response": 500})
    apilogger.info("Successful scan")

    return jsonify({"response": 200})

@app.route('/login')
def login():
    return github.authorize(scope="user,repo")

@app.route('/callback')
@github.authorized_handler
def authorized(oauth_token):
    next_url = 'http://localhost/'
    if oauth_token is None:
        flash("Authorization failed.")
        return jsonify({"response": 500})

    try:
        user = db.user.find_one({
        'github_access_token': oauth_token
    })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return jsonify({"response": 500})
    
    if user is None:
        user_info = requests.get('https://api.github.com/user', auth=('token',oauth_token))
        json_info = user_info.json()
        username = json_info['login']
        update_query = {
        '$set':{
               'github_access_token': oauth_token
               }
        }
        user = db.user.update({
            'github_username': username
        },
                       update_query,upsert=True)
    
    return redirect(next_url+'?login={}'.format(username))

@app.route('/logout/<username>')
def logout(username):
    try:
        db.user.update({
            'github_username': username 
        },{'$unset': {
            'github_access_token': 1
        }
        })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return jsonify({"response": 500})

    return redirect("http://localhost/")

@app.route('/seq')
def last_seq_number():
    try:
        ret = db.counters.find_and_modify(query={
                     '_id': 'userid' }, update=
                    {'$inc': { 'seq': 1 }}, upsert=True)
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return jsonify({"response": 500})

    return jsonify({'seq':ret['seq']})

@app.route('/check/<username>')
def check_token(username):
    try:
        user = db.user.find_one({
        'github_username': username
    })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return jsonify({"response":500})

    if user is None:
        return jsonify({'response':404})
    if "github_access_token" not in user:
        return jsonify({"response":401})

    res = requests.get('https://api.github.com/applications/{}/tokens/{}'.format(
    app.config['GITHUB_CLIENT_ID'], user['github_access_token']), 
    auth=(app.config['GITHUB_CLIENT_ID'], app.config['GITHUB_CLIENT_SECRET'])
    )

    if res.status_code == 200:
        return jsonify({"response":200})
    else:
        return jsonify({"response":500})

@app.route('/resource', methods=['POST'])
def insert_resource():
    print(request)
    if request.method != "POST":
        return ({"response":405})    
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"response":400})
        insert_data = {
            'res_id': int(data['res_id']),
            'title': data['title'],
            'url': data['url'],
            'language': data['language'],
            'level': data['level'],
            'created_by': data['created_by']
            }
        try:
            db.resource.insert_one(insert_data)
        except pm.errors.OperationFailure as err:
            logger.error(err)
            return jsonify({"response":500})

        return redirect("http://localhost/?login={}".format(data['created_by']))

@app.route('/resource/read/<res_id>', methods=['POST'])
def mark_as_read(res_id):
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"response":400})
        try:
            db.resource.update({  
                    'res_id': int(res_id)
                },
                {  
                    '$addToSet': {
                        'read_by': data['read_by']
                    }
                }
            )
        except pm.errors.OperationFailure as err:
            logger.error(err)
            return jsonify({"response":500})
        
        try:
            db.user.update({
                    'github_username':data['read_by'],
                    'new_reading_list':{
                        '$elemMatch':{
                            'res_id':int(res_id)
                        }
                    }
                },
                {
                    '$addToSet':{  
                        'new_reading_list.$.read_by':data['read_by']
                    }
                }
            )

        except pm.errors.OperationFailure as err:
            logger.error(err)
            return jsonify({"response":500})

        try:
            db.user.update({
                    'github_username':data['read_by'],
                    'last_reading_list':{
                        '$elemMatch':{
                            'res_id':int(res_id)
                        }
                    }
                },
                {
                    '$addToSet':{
                        'last_reading_list.$.read_by':data['read_by']
                    }
            })
        except pm.errors.OperationFailure as err:
            logger.error(err)
            return jsonify({"response":500})

        try:
            res = db.resource.find_one({
                    'res_id': int(res_id)
                }
            )
            db.user.update({
                    'github_username': data['read_by']
                },
                {
                    '$addToSet': {
                        'read': res
                    }
                }
            )
        except pm.errors.OperationFailure as err:
            logger.error(err)
            return jsonify({"response":500})
    return redirect("http://localhost/?login={}".format(data['read_by']))


app.wsgi_app = DispatcherMiddleware(run_simple, {'/api': app.wsgi_app})

if __name__ == '__main__':
    app.run(threaded=True)

