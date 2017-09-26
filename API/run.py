from eve import Eve
from scanner import *


app = Eve()

@app.route('/scan/<git_username>')
def launch_scan(git_username):

	scan_result = manual_scan(git_username)
	if (scan_result == 1):
		return "Success"
	else:
		return "Error"


if __name__ == '__main__':
    app.run()
