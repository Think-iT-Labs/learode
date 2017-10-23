#Fetch user info
from db_connection import db_connect
from log_script import create_logger


db = db_connect()
logger = create_logger()


##Insert test_user
test_user_query = [
    {
        "user_id":  558,
        "github_username":  "this_is_a_test_subject",
        "token":  "f8fa8a07",
        "new_reading_list":  [
        ],
        "last_reading_list":  [
        ]
    }
]

logger.info("Inserting test_user")

try:
    db.user_collection.insert(test_user_query)
except pm.errors.OperationFailure as err:
    logger.error(err)
    return False

## Fetch test_user
logger.info("Fetching test_user")

try:
    test_user = db.user.find_one({
        "user_id":  558
    })
except pm.errors.OperationFailure as err:
    logger.error(err)
    return False

if test_user is None:
    logger.error("Couldn't find user")
    return False

assert test_user['github_username'] == 'this_is_a_test_subject'
assert test_user['token'] == 'f8fa8a07'

logger.info("Removing test_user")

try:
    test_user = db.user.remove({
        "user_id":  558
    })
except pm.errors.OperationFailure as err:
    logger.error(err)
    return False

try:
    test_user = db.user.find_one({
        "user_id":  558
    })
except pm.errors.OperationFailure as err:
    logger.error(err)
    return False

assert test_user is None

logger.info("All tests passed!")
