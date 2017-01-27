import json
import sys
import requests
	
def getdevicelist(server,username,password):
	auth_token = ''
	auth_url = server + "/api/fmc_platform/v1/auth/generatetoken"
	r = None
	headers = {'Content-Type': 'application/json'}
	try:
		r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)
		#r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify='/path/to/ssl_certificate')
		auth_headers = r.headers
		auth_token = auth_headers.get('X-auth-access-token', default=None)
	except:
		"error occurred, check server name, username and password passed to function"
	headers['X-auth-access-token']=auth_token
	devices = ''
	devicelist = []
	url = server + "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devices/devicerecords"
	if (url[-1] == '/'):
		url = url[:-1]
	print auth_token
	try:
    # REST call with SSL verification turned off: 
		r = requests.get(url, headers=headers, verify=False)
		# REST call with SSL verification turned on:
		#r = requests.get(url, headers=headers, verify='/path/to/ssl_certificate')
		status_code = r.status_code
		resp = r.text
		if (status_code == 200):
			print("GET successful.")
			json_resp = json.loads(resp)
			devices = (json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
		else:
			r.raise_for_status()
			print("Error occurred in GET --> "+resp)
	except requests.exceptions.HTTPError as err:
		print ("Error in connection --> "+str(err)) 
	finally:
		if r : r.close()
	for line in devices.split("\n"):
		if "name" in line:
			line = line.replace("name",'')
			line = line.replace('"','')
			line = line.replace(' ','')
			line = line.replace(":","")
			line = line.replace(",","")
			devicelist.append(line)
	for name in devicelist:
		print name
	return devicelist

