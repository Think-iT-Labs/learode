import os, sys
import requests
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_script import create_logger


logger = create_logger()

print("Running Endpoint Tester....\n")
address = input("Enter the server's address\n Default: 'http://localhost:5000':   ")
if address == '':
    address = 'http://localhost:5000'


### Test scan

print("Making a get request to /scan...")
res = None
url = address + "/scan/SynergySINE"
try:
    res = requests.get(url, timeout=15)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

json_res = res.json()

assert json_res['response'] == 200


### test fetch user
print("Making a GET request to /user...")
res = None
url = address + "/user/SynergySINE"
try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

json_res = res.json()

assert json_res['github_username'] == "SynergySINE"

### test fetch resource
print("Making a GET request to /resource...")
res = None
url = address + "/resource/1"
try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    raise ValueError("Variable Res == False")

json_res = res.json()

assert json_res['title'] == "Intermediate Python"

### test insert resource
#print("Making a POST request to /resource...")
#res = None
#url = address + "/resource/1"
#try:
#    res = requests.get(url, timeout=5)
#    res.raise_for_status()
#except Exception as err:
#    logger.error(err)

#if not res:
#    raise ValueError("Variable Res == False")


#json_res = res.json()

#assert json_res['response'] == 200

### test insert user
#print("Making a POST request to /user...")
#res = None
#url = address + "/user/1"
#try:
#    res = requests.get(url, timeout=5)
#    res.raise_for_status()
#except Exception as err:
#   logger.error(err)

#if not res:
#    raise ValueError("Variable Res == False")


#json_res = res.json()

#assert json_res['response'] == 200

print("All tests successful !")
