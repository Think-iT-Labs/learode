import os, sys
import requests
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_script import create_logger
from db_connection import db_connect

db = db_connect()
logger = create_logger()

print("Running Endpoint Tester....\n")
address = input("Enter the server's address\n Default: 'http://localhost:5000':   ")
if address == '':
    address = 'http://localhost:5000'
test_username = "SynergySINE"

### Test scan

print("Making a GET request to /scan...")
res = None
url = address + "/scan/{}".format(test_username)
try:
    res = requests.get(url, timeout=30)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

json_res = res.json()
print(json_res)
assert json_res['response'] == 200


### test fetch user
print("Making a GET request to /user...")
res = None
url = address + "/user/{}".format(test_username)
try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

json_res = res.json()

assert json_res['github_username'] == test_username

### test fetch resource
print("Making a GET request to /resource...")
res = None
url = address + "/resource/1"
try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

json_res = res.json()

assert json_res['title'] == "Intermediate Python"


### test check token

print("Making a GET request to /check...")
res = None

url = address + "/check/{}".format(test_username)
try:
    res = requests.get(url, timeout=30)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

json_res = res.json()

assert json_res['response'] == 200


### test logout

print("Making a GET request to /logout...")
res = None

url = address + "/logout/{}".format(test_username)
try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

try:
    user = db.user.find_one({
        'github_username': test_username
    })
except pm.errors.OperationFailure as err:
    logger.error(err)
    raise ValueError("Error accessing database")

assert res.status_code == 200
assert 'github_access_token' not in user

### test seq
print("Making a GET request to /seq...")
res = None

url = address + "/seq"
try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

try:
    seq_number = db.counters.find_one()
except pm.errors.OperationFailure as err:
    logger.error(err)
    raise ValueError("Error accessing database")

assert res.status_code == 200
assert seq_number['userid']

### test check
print("Making a GET request to /check...")
res = None

url = address + "/check/{}".format(test_username)
try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

assert res.status_code == 200
json_res = res.json()
assert json_res['response'] == 200

print("All tests successful !")
