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
        "github_access_token":  "",
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
        "url": "https://www.packtpub.com/big-data-and-business-intelligence/python-end-end-data-analysis",
        "language": "python",
        "level": "medium",
	"read_by": []
    },
    {
        "res_id": 3,
        "title": "Learning Javascript",
        "url": "https://www.amazon.co.uk/Learning-JavaScript-Shelley-Powers/dp/8184042159",
        "language": "javascript",
        "level": "beginner";
	"read_by": []
    },
    {
        "res_id": 4,
        "title": "Learn HTML at MDN",
        "url": "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article",
        "language": "html",
        "level": "beginner",
	"read_by": []
    },    {
        "res_id": 5,
        "title": "Introduction to CSS at MDN",
        "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS",
        "language": "css",
        "level": "beginner",
	"read_by": []
    },    {
        "res_id": 6,
        "title": "Introduction to CSS at CSSTutorial.net",
        "url": "https://www.csstutorial.net/css-intro/introductioncss-part1.php",
        "language": "css",
        "level": "beginner",
	"read_by": []
    },    {
        "res_id": 7,
        "title": "Sass basics",
        "url": "http://sass-lang.com/guide",
        "language": "css",
        "level": "intermediate",
	"read_by": []
    },    {
        "res_id": 8,
        "title": "CSS Advanced",
        "url": "http://marksheet.io/css-advanced.html",
        "language": "css",
        "level": "advanced",
	"read_by": []
    },    {
        "res_id": 9,
        "title": "Complete C# tutorial",
        "url": "http://csharp.net-tutorials.com/basics/introduction/",
        "language": "csharp",
        "level": "beginner",
	"read_by": []
    },    {
        "res_id": 10,
        "title": "Interactive C# tutorial at learncs.org",
        "url": "http://www.learncs.org/",
        "language": "csharp",
        "level": "beginner",
	"read_by": []
    },    {
        "res_id": 11,
        "title": "Intermediate C# tutorials",
        "url": "http://rbwhitaker.wikidot.com/c-sharp-intermediate-tutorials",
        "language": "csharp",
        "level": "intermediate",
	"read_by": []
    },    {
        "res_id": 12,
        "title": "Advanced C#",
        "url": "http://www.ssw.uni-linz.ac.at/Teaching/Lectures/CSharp/Tutorial/Part2.pdf",
        "language": "csharp",
        "level": "advanced",
	"read_by": []
    },    {
        "res_id": 13,
        "title": "Learn Perl",
        "url": "http://www.learn-perl.org/",
        "language": "perl",
        "level": "beginner",
	"read_by": []
    },    {
        "res_id": 14,
        "title": "Learn C",
        "url": "http://www.learn-c.org/",
        "language": "c",
        "level": "beginner",
	"read_by": []
    },    {
        "res_id": 15,
        "title": "Guide to Advanced Programming in C",
        "url": "http://pfacka.binaryparadise.com/articles/guide-to-advanced-programming-in-C.html",
        "language": "c",
        "level": "advanced",
	"read_by": []
    },    {
        "res_id": 16,
        "title": "Advanced C",
        "url": "https://www.e-reading.club/bookreader.php/138793/Advanced_C.pdf",
        "language": "c",
        "level": "advanced",
	"read_by": []
    },    {
        "res_id": 17,
        "title": "Agile Development Using Ruby on Rails - Advanced",
        "url": "https://www.edx.org/course/agile-development-using-ruby-rails-uc-berkeleyx-cs169-2x-0",
        "language": "ruby",
        "level": "advanced",
	"read_by": []
    },    {
        "res_id": 18,
        "title": "Intro to React",
        "url": "https://reactjs.org/tutorial/tutorial.html",
        "language": "javascript",
        "level": "beginner",
	"read_by": []
    },    {
        "res_id": 19,
        "title": "Advanced React and Redux",
        "url": "https://www.udemy.com/react-redux-tutorial/",
        "language": "javascript",
        "level": "advanced",
	"read_by": []
    },

]

try:
    db.resource_collection.insert_many(test_resource_query)
except pm.errors.OperationFailure as err:
    print(err)

try:
    db.user_collection.insert_many(test_user_query)
except pm.errors.OperationFailure as err:
    print(err)
