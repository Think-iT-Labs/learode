
import requests
import json
from db_connection import *


def gitScan(user,db):
	url='https://api.github.com/'
	#try:
	#	token = db.user.find_one({'github_username':user},{'token':1,'_id':0})
	#except pm.errors.OperationFailure as e:
	#	print(e)
	authtoken='token 0b98eba02250b467432dcefa32473d95f8fa8a07' #+ token['token']
	try:
		responseUserRepoList = requests.get(url+'users/'+user+'/repos', headers={'Authorization': authtoken})
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)	
	languages=[]
	jsonUserRepoList=responseUserRepoList.json()	
	print("fetching languages url")
	for repo in jsonUserRepoList:
		try:		
			responseuserlanguagelist=requests.get(repo["languages_url"], headers={'Authorization': authtoken})
		except requests.exceptions.RequestException as e:
			print(e)
			sys.exit(1)
		jsonUserLanguageList=responseuserlanguagelist.json()		
		languages.append(jsonUserLanguageList)
	userlanguages= set(k.lower() for d in languages for k in d.keys())
	return userlanguages


def FetchAvailableResources(language,db):
	print("fetching: " + language)
	av_res=[]
	try:
		cur_av_res = db.resource.find({"language":language})	
	except pm.errors.OperationFailure as e:
		print(e)	
	for item in cur_av_res:
		av_res.append(item)
	return av_res 


def CreateNewRL(userlanguages,db):
	reslist=[]
	for language in userlanguages:
		reslist.append(FetchAvailableResources(language,db))
	return reslist


def StoreRL(tmpRL,username,db):
	try:
		responseuser = db.user.find_one({'github_username':username})
	except pm.errors.OperationFailure as e:
		print(e)	
	if (responseuser!=None):
		tmp_db_rl = responseuser['new_reading_list']
	else:
		tmp_db_rl=[]
	RL = [item for sublist in tmpRL for item in sublist]
	try:
		db.user.update({'github_username':username,},{'$set':{'last_reading_list':tmp_db_rl,'new_reading_list':RL}},upsert=True)
	except pm.errors.OperationFailure as e:
		print(e)


def GetUserInfo(db):
	try:
		userList = db.user.find({'github_username':1, 'token':1})
	except pm.errors.OperationFailure as e:
		print(e)
	if (userList.count()!=0):	
		jsonUserList = userList.json()
	return jsonUserList

def manualScan(user,db=None):
	if (db==None):
		db = dbconnect()
	print("Scanning...")
	gitresults = gitScan(user,db)
	print("Finished scanning !")
	print("Connecting...")
	print("Connected !")
	print("Creating new reading list...")
	readinglist = CreateNewRL(gitresults,db)
	print("Finished creating new reading list")
	print("Storing...")
	StoreRL(readinglist,user,db)
	print("Done storing !")
	print("Finished running.")
	return "Finished successfully"

def automaticScan():
	db = dbconnect()
	UserList=GetUserInfo(db)
	for user in UserList:
		manualScan(user['github_username'],db)
