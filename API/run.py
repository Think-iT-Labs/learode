from eve import Eve
from flask import jsonify, request, url_for, redirect
from flask_github import GitHub



import requests
import json

from scanner import *
from log_script import create_logger

assert db is not None

app = Eve()
app.config['GITHUB_CLIENT_ID'] = '' #client_id
app.config['GITHUB_CLIENT_SECRET'] = '' #client_secret

github = GitHub(app)

username = ""

@app.route('/scan/<git_username>')
def launch_scan(git_username):
    apilogger = create_logger()
    if not manual_scan(git_username):
        apilogger.error("Manual scan failed")
        return jsonify({"response":500})
    apilogger.info("Successful scan")
    return jsonify({"response":200})

@app.route('/login/<github_username>')
def login(github_username):
    global username
    username = github_username
    return github.authorize()

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
        global username
        update_query = {
        '$set':{
               'github_access_token': oauth_token
               }
        }
        user = db.user.update({
            'github_username': username
        },
                       update_query, upsert=True)
    return redirect(next_url)

if __name__ == '__main__':
    app.run()
