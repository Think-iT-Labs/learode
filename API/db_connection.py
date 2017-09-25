import pymongo as pm
def dbconnect():
	client=pm.MongoClient('localhost', 27017) #connecting to mongodb
	db=client['Learode'] #connecting to database
	return db
