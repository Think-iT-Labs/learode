import requests
import json

from db_connection import *
from log_script import *


logger = create_logger()
url='https://api.github.com'
db = db_connect()

def request_git_api(request_url)
    auth_h={'Authorization': 'token 0b98eba02250b467432dcefa32473d95f8fa8a07'}
    try:
        tmp = requests.get(request_url, headers=auth_header, timeout=5)
        tmp.raise_for_status()
    except Exception as err:
        logger.error(err)

    return tmp


def git_scan(user):
    request_url = '{}/users/{}/repos'.format(url, user)
    response_user_repo_list = request_git_api(request_url)
    languages = []
    json_user_repo_list = response_user_repo_list.json()    
    logger.info("fetching languages url")
    for repo in json_user_repo_list:
        response_user_language_list = requests_git_api(repo["languages_url"])
        json_user_language_list = response_user_language_list.json()        
        languages.append(json_user_language_list)

    user_languages= set(k.lower() for d in languages for k in d.keys())

    return user_languages


def fetch_available_resources(language):
    logger.info("fetching: " + language)
    available_resources=[]

    try:
        current_available_resources = db.resource.find({"language": language})
    except pm.errors.OperationFailure as err:
        logger.error(err)    

    for item in current_available_resources:
        available_resources.append(item)

    return available_resources


def create_reading_list(user_languages):
    resource_list=[]
    for language in user_languages:
        resource_list.append(fetch_available_resources(language))
    
    return resource_list


def store_reading_list(tmp_reading_list,username):
    try:
        response_user = db.user.find_one({'github_username': username})
    except pm.errors.OperationFailure as err:
        logger.error(err)    

    if (response_user != None):
        tmp_db_rl = response_user['new_reading_list']
    else:
        tmp_db_rl = []

    reading_list = [item for sublist in tmp_reading_list for item in sublist]
    update_query = {'$set': {'last_reading_list': tmp_db_rl, 
                             'new_reading_list':  reading_list}}
    try:
        db.user.update({'github_username': username}, 
                       update_query, upsert=True)
    except pm.errors.OperationFailure as err:
        logger.error(err)


def get_user_info():
    try:
        user_list = db.user.find({'github_username': 1, 'token': 1})
    except pm.errors.OperationFailure as err:
        logger.error(err)

    if (user_list.count() != 0):    
        json_user_list = user_list.json()

    return json_user_list


def manual_scan(user):
    logger = create_logger()
    git_results = git_scan(user)
    logger.info("Finished scanning")
    reading_list = create_reading_list(git_results)
    logger.info("Finished creating new reading list")
    store_reading_list(reading_list, user)

    return True


def automatic_scan():
    user_list = get_user_info()
    for user in user_list:
        manual_scan(user['github_username'])
