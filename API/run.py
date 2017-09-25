from eve import Eve
from Scanner import *

app = Eve()
@app.route('/scan/<git_username>')
def launchScan(git_username):
	scanresult = manualScan(git_username)
	if (scanresult == 1):
		return "Success"
	else:
		return "Error"
if __name__ == '__main__':
    app.run()
