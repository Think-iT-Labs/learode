from eve import Eve
from flask import jsonify, request, url_for, redirect, flash
from flask_github import GitHub
from flask_cors import CORS


import requests
import json

from scanner import *
from log_script import create_logger

assert db is not None

app = Eve()
app.config['GITHUB_CLIENT_ID'] = ''
app.config['GITHUB_CLIENT_SECRET'] = ''
app.config['SECRET_KEY'] = ''

github = GitHub(app)
CORS(app)

username = ""

@app.route('/scan/<git_username>')
def launch_scan(git_username):
    apilogger = create_logger()
    if not manual_scan(git_username):
        apilogger.error("Manual scan failed")
        return jsonify({"response":500})
    apilogger.info("Successful scan")
    return jsonify({"response":200})

@app.route('/login')
def login():
    return github.authorize(scope="user,repo")

@app.route('/callback')
@github.authorized_handler
def authorized(oauth_token):
    next_url = 'http://localhost:8080/'
    if oauth_token is None:
        flash("Authorization failed.")
        return jsonify({"response":500})

    try:
        user = db.user.find_one({
        'github_access_token': oauth_token
    })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return False
    
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
                       update_query, upsert=True)
    
    return redirect(next_url+'?login={}'.format(username))

@app.route('/logout/<username>')
def logout(username):
    try:
        db.products.update({
            'github_username': username 
        },{'$unset': {
            'github_access_token': ""
        }
        })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return False
    return redirect("http://localhost:8080")

@app.route('/check/<username>')
def check_token(username):
    try:
        user = db.user.find_one({
        'github_username': username
    })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return False

    if user is None:
        return jsonify({'response':404})

    res = requests.get('https://api.github.com/applications/{}/tokens/{}'.format(app.config['GITHUB_CLIENT_ID'], user['github_access_token']), auth=(app.config['GITHUB_CLIENT_ID'], app.config['GITHUB_CLIENT_SECRET']))
    print(res.status_code)

    if res.status_code == 200:
        return jsonify({"response":200})
    else:
        return jsonify({"response":500})

if __name__ == '__main__':
    app.run(threaded=True)

