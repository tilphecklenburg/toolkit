import requests

def panosapi_genapikey(devip,username,password):
	panapikey = requests.get("https://" + devip + "/api/?type=keygen&user=" + username + "&password=" + password, verify=False)
	apikey = str(panapikey.text)
	apikey = apikey.replace("<response status = 'success'><result><key>","")
	apikey = apikey.replace("</key></result></response>","")
	return apikey