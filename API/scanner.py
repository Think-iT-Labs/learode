import requests
import json
from db_connection import *


def git_scan(user,db):

	url='https://api.github.com/'
	auth_token='token 0b98eba02250b467432dcefa32473d95f8fa8a07'

	try:
		response_user_repo_list = requests.get(url+'users/'+user+'/repos', headers={'Authorization': auth_token})
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)	
	languages=[]
	json_user_repo_list=response_user_repo_list.json()	

	print("fetching languages url")
	for repo in json_user_repo_list:
		try:		
			response_user_language_list=requests.get(repo["languages_url"], headers={'Authorization': auth_token})
		except requests.exceptions.RequestException as e:
			print(e)
			sys.exit(1)
		json_user_language_list=response_user_language_list.json()		
		languages.append(json_user_language_list)

	user_languages= set(k.lower() for d in languages for k in d.keys())
	return user_languages


def fetch_available_resources(language,db):

	print("fetching: " + language)
	available_resources=[]

	try:
		current_available_resources = db.resource.find({"language":language})	
	except pm.errors.OperationFailure as e:
		print(e)	

	for item in current_available_resources:
		available_resources.append(item)

	return available_resources


def create_new_rl(user_languages,db):

	reslist=[]
	for language in user_languages:
		resource_list.append(fetch_available_resources(language,db))
	return resource_list


def store_rl(tmp_reading_list,username,db):

	try:
		response_user = db.user.find_one({'github_username':username})
	except pm.errors.OperationFailure as e:
		print(e)	

	if (response_user!=None):
		tmp_db_rl = response_user['new_reading_list']
	else:
		tmp_db_rl=[]

	reading_list = [item for sublist in tmp_reading_list for item in sublist]

	try:
		db.user.update({'github_username':username,},{'$set':{'last_reading_list':tmp_db_rl,'new_reading_list':reading_list}},upsert=True)
	except pm.errors.OperationFailure as e:
		print(e)
	#Will try to update the document having that username with a new reading list, and will put the old reading list in its last_reading_list field. 
	#If there's no such document, will create one with upsert=True 

def get_user_info(db):

	try:
		user_list = db.user.find({'github_username':1, 'token':1})
	except pm.errors.OperationFailure as e:
		print(e)

	if (user_list.count()!=0):	
		json_user_list = user_list.json()
	return json_user_list


def manual_scan(user,db=None):

	if (db==None):
		db = db_connect()
	print("Scanning...")
	git_results = git_scan(user,db)
	print("Finished scanning !")
	print("Connecting...")
	print("Connected !")
	print("Creating new reading list...")
	reading_list = create_new_rl(git_results,db)
	print("Finished creating new reading list")
	print("Storing...")
	store_rl(reading_list,user,db)
	print("Done storing !")
	print("Finished running.")
	return "Finished successfully"


def automatic_scan():

	db = db_connect()
	user_list=get_user_info(db)
	for user in user_list:
		manual_scan(user['github_username'],db)
