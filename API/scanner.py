import requests
import json

from db_connection import db_connect
from log_script import create_logger

url = 'https://api.github.com'
db = db_connect()
logger = create_logger()

def get_access_token(username):
    try:
        user = db.user.find_one({
        'github_username': username
    })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return None

    if 'github_access_token' not in user:
        return False

    return user['github_access_token']

def request_git_api(request_url, access_token):
    res = None

    try:
        res = requests.get(request_url, timeout=15, auth=('token',access_token))
        res.raise_for_status()
    except Exception as err:
        logger.error(err)
        return None

    return res


def git_scan(user):
    request_url = '{}/users/{}/repos'.format(url, user)

    access_token = get_access_token(user)
    if access_token is None:
        logger.error("User not authentified")
        return False

    res_user_repos = request_git_api(request_url, access_token)
    
    if not res_user_repos:
        return False
    json_user_repos = res_user_repos.json()

    logger.info("fetching languages url")
    res_user_languages = []
    languages = []
    for repo in json_user_repos:
        res_user_languages = request_git_api(repo["languages_url"], access_token)
        if not res_user_languages:
            continue
        json_user_languages = res_user_languages.json()
        languages.append(json_user_languages)

    user_languages = set(k.lower() for d in languages for k in d.keys())

    return user_languages


def fetch_available_resources(language):
    logger.info("fetching: " + language)
    available_resources = []
    current_available_resources = []
    try:
        current_available_resources = db.resource.find({
        'language': language
    })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return False

    for item in current_available_resources:
        available_resources.append(item)

    return available_resources


def create_reading_list(user_languages):
    resource_list = []
    for language in user_languages:
        result = fetch_available_resources(language)
        if result == False:
            return False
        resource_list.append(result)

    return resource_list


def store_reading_list(tmp_reading_list, username):
    try:
        response_user = db.user.find_one({
        'github_username': username
    })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return False

    if response_user is not None:
        tmp_db_rl = response_user['new_reading_list']
    else:
        return False

    reading_list = [item for sublist in tmp_reading_list for item in sublist]
    update_query = {
        '$set':{
            'last_reading_list': tmp_db_rl,
            'new_reading_list': reading_list
        }
    }
    try:
        db.user.update({
            'github_username': username
        },
                       update_query, upsert=True)
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return False

    return True


def get_user_info():
    try:
        user_list = db.user.find({
            'github_username': True,
            'token': True
        })
    except pm.errors.OperationFailure as err:
        logger.error(err)
        return False

    if len(user_list) != 0:
        json_user_list = user_list.json()

    return json_user_list


def manual_scan(user):
    git_results = git_scan(user)
    if not git_results:
        logger.error("git_scan() returned False")
        return False

    logger.info("Finished scanning")

    reading_list = create_reading_list(git_results)
    if not reading_list:
        logger.error("create_reading_list() returned False")
        return False

    logger.info("Finished creating new reading list")
    result = store_reading_list(reading_list, user)
    if not result:
        logger.error("store_reading_list() returned False")

    return True


def automatic_scan():
    user_list = get_user_info()
    if not user_list:
        logger.error("get_user_info() returned False")
        return False
    for user in user_list:
        manual_scan(user['github_username'])
         
