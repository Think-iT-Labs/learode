import pymongo as pm


try:
    client = pm.MongoClient('localhost', 27017)
except pm.errors.ConnectionFailure as err:
    print('''Error connecting to the Mongo Client,
          check if your mongod service is started''')

db = client.Learode
user_collection = db.user
resource_collection = db.resource

test_user_query = [
    {
        "user_id":  1,
        "github_username":  "SynergySINE",
        "token":  "0b98eba02250b467432dcefa32473d95f8fa8a07",
        "new_reading_list":  [
        ],
        "last_reading_list":  [
        ]
    }
]

test_resource_query = [
    {
        "res_id": 1,
        "title": "Intermediate Python",
        "url": "http: //www.book.pythontips.com",
        "language": "python",
        "level": "medium",
	"read_by": []
    },
    {
        "res_id": 2,
        "title": "Python End-to-End Data analysis",
        "url": "https: //www.packtpub.com/big-data-and-business-intelligence/python-end-end-data-analysis",
        "language": "python",
        "level": "medium",
	"read_by": []
    },
    {
        "res_id": 3,
        "title": "Learning Javascript",
        "url": "https: //www.amazon.co.uk/Learning-JavaScript-Shelley-Powers/dp/8184042159",
        "language": "javascript",
        "level": "beginner";
	"read_by": []
    },
    {
        "res_id": 4,
        "title": "Learn HTML at MDN",
        "url": "https: //developer.mozilla.org/en-US/docs/Web/HTML/Element/article",
        "language": "html",
        "level": "beginner",
	"read_by": []
    }
]

try:
    db.resource_collection.insert_many(test_resource_query)
except pm.errors.OperationFailure as err:
    print(err)

try:
    db.user_collection.insert_many(test_user_query)
except pm.errors.OperationFailure as err:
    print(err)
