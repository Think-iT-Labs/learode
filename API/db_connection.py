import pymongo as pm


def db_connect():
    try:
        client = pm.MongoClient('localhost', 27017)
    except pm.errors.ConnectionFailure as err:
        print("Can't connect")
    db = client['Learode']
    return db
