from eve import Eve

from scanner import *
from log_script import *


app = Eve()


@app.route('/scan/<git_username>')
def launch_scan(git_username):
    if (manual_scan(git_username) != 0):
        apilogger = create_logger()
        apilogger.error("Manual scan failed")
        return 1
    print("Success")
    return 0

if __name__ == '__main__':
    app.run()
