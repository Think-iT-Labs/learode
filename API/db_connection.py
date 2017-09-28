import pymongo as pm


def db_connect():
    try:
        client=pm.MongoClient('localhost', 27017)
    except pymongo.errors.ConnectionFailure as err:
    db=client['Learode']

    return db
