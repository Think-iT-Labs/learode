import pymongo as pm


def db_connect():

	client=pm.MongoClient('localhost', 27017) #connecting to mongodb
	db=client['Learode'] #connecting to database
	return db
