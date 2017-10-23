from eve import Eve

from scanner import manual_scan
from log_script import create_logger


app = Eve()


@app.route('/scan/<git_username>')
def launch_scan(git_username):
    if not manual_scan(git_username):
        apilogger = create_logger()
        apilogger.error("Manual scan failed")
        return True
    apilogger.info("Successful scan")
    return False

if __name__ == '__main__':
    app.run()
