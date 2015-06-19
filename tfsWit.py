__author__ = 'Administrator'

import requests
import json
from requests.auth import HTTPBasicAuth
import os
import sys
import datetime

svnRepo = sys.argv[1]
svnRev = sys.argv[2]
svnTxn = sys.argv[3]
command = "svnlook log " + svnRepo + " -r " + svnRev
svnLog = os.popen(command).read()
command = "svnlook author " + svnRepo + " -r " + svnRev
svnInfo = os.popen(command).read()
command = "svnlook changed " + svnRepo + " -r " + svnRev
svnChanged = os.popen(command).read()
i=datetime.datetime.now()
svnInfo = svnInfo + "   %s" %i + "  SVN Rev:"+ svnRev + "  Comments:" + svnLog.split(":")[1] + "<br>"
#init TFS connection
tfsCollection = 'https://xhvso.visualstudio.com/DefaultCollection/'
tfsProject = 'xhpiproj'
tfsWit = '/_apis/wit/workitems/' + svnLog.split(":")[0]
apiVersion = '?api-version=1.0'
tfsUser = 'haxu'
tfsPass = '!@#QWEasdzxc'
headers = {'Content-Type': 'application/json-patch+json'}

#get lastest rev number
getWit = requests.get(tfsCollection + tfsWit + apiVersion, auth=HTTPBasicAuth(tfsUser, tfsPass))
#revNum = getWit.json()["rev"]
getWit.json()['value'][0]['rev']
#oldDescription = getWit.json()["Sysyem.Description"]
filedData = {"op":"test","path":"/rev","value": revNum}, {"op": "add", "path": "/fields/System.Description", "value": svnInfo}, {"op": "add", "path": "/fields/System.History", "value": svnChanged}

#update work item filed 
requests.patch(tfsCollection + tfsWit + apiVersion, data=json.dumps(filedData), headers=headers, auth=HTTPBasicAuth(tfsUser, tfsPass))
