__author__ = 'Xu Hao'

import requests
import json
from requests.auth import HTTPBasicAuth
import os
import sys

#Ops Function
#createProj()

#getWitRev()
#get lastest rev number
def getWitRev(tfsCollection,witId,tfsUser,tfsPass):
	apiVersion = '?api-version=1.0'
	apiPath = '/_apis/wit/workitems/'
	url = tfsCollection + apiPath + str(witId) + apiVersion
	getWit = requests.get(url, auth=HTTPBasicAuth(tfsUser, tfsPass))
	return getWit.json()['rev']

#patchWit()
def patchWit(tfsCollection,witId,tfsUser,tfsPass,patchData):
	headers = {'Content-Type': 'application/json-patch+json'}
	apiVersion = '?api-version=1.0'
	apiPath = '/_apis/wit/workitems/'
	url = tfsCollection + apiPath + str(witId) + apiVersion
	requests.patch(url, data=json.dumps(patchData), headers=headers, auth=HTTPBasicAuth(tfsUser, tfsPass))

#build()

#release

if __name__ == '__main__' :
	#init TFS connection
	tfsCollection = 'http://192.168.1.11:8080/tfs/DefaultCollection/'
	#tfsProject = 'xhpiproj'
	tfsUser = 'administrator'
	tfsPass = '!@#QWEasdzxc'
	witId = 67
	revNum = getWitRev(tfsCollection,witId,tfsUser,tfsPass)
	filedData = {"op":"test","path":"/rev","value": revNum}, {"op": "add", "path": "/fields/System.Description", "value": sys.argv[1]}, {"op": "add", "path": "/fields/System.History", "value": sys.argv[2]}
	patchWit(tfsCollection,witId,tfsUser,tfsPass,filedData)
	