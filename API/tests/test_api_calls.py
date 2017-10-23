import requests
import json
import sys

from log_script import create_logger

logger = create_logger()

print("Running Endpoint Tester....\n")
address = raw_input("Enter the server's address\n Default: 'http://localhost:5000':   ")
if address == '':
    address = 'http://localhost:5000'


# Test scan

print("Making a GET request to /scan...")

    url = address + "/scan/SynergySINE"
	try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
    except Exception as err:
        logger.error(err)

    if not res:
        return None

    json_res = res.json()
    assert res['response'] == True


# test fetch user
print("Making a GET request to /user...")
url = address + "/user/SynergySINE"
try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    return None
json_res = res.json()
assert json_res['github_username'] == "SynergySINE"

# test fetch resource
print("Making a GET request to /resource...")

url = address + "/resource/1"
try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    return None
json_res = res.json()
assert json_res['title'] == "Intermediate Python"

# test insert resource
print("Making a POST request to /resource...")

url = address + "/resource/1"
try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    return None
json_res = res.json()
assert json_res['response'] == True

# test insert user
print("Making a POST request to /user...")

url = address + "/user/1"
try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
except Exception as err:
    logger.error(err)

if not res:
    return None
json_res = res.json()
assert json_res['response'] == True

