from eve import Eve
from flask import jsonify
import json

from scanner import *
from log_script import create_logger


app = Eve()


@app.route('/scan/<git_username>')
def launch_scan(git_username):
    apilogger = create_logger()
    if not manual_scan(git_username):
        apilogger.error("Manual scan failed")
        return jsonify({"response":500})
    apilogger.info("Successful scan")
    return jsonify({"response":200})

if __name__ == '__main__':
    app.run()
