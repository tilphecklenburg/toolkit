import requests
import re
from time import gmtime, strftime
import os

def genapikey(devip,username,password):
	panapikey = requests.get("https://" + devip + "/api/?type=keygen&user=" + username + "&password=" + password, verify=False)
	apikey = str(panapikey.text)
	apikey = apikey.replace("<response status = 'success'><result><key>","")
	apikey = apikey.replace("</key></result></response>","")
	return apikey
	
def getifaceinfo(devip,apikey):
	interfaceinfo = requests.get("https://" + devip + "/api/?type=config&action=get&key=" + apikey + "&xpath=/config/devices/entry[@name='localhost.localdomain']/network/interface/ethernet", verify=False)
	return interfaceinfo.text
	
def getbandwidth(devip,apikey):
	interfaceinfo = requests.get("https://" + devip + "/api/?&type=op&cmd=%3Cshow%3E%3Cqos%3E%3Cinterface%3Eethernet1%2F1%3C%2Finterface%3E%3Cthroughput%3E0%3C%2Fthroughput%3E%3C%2Fqos%3E%3C%2Fshow%3E&key=" + apikey, verify=False)
	return interfaceinfo.text
	
def savebandwidthtocsv(interfaceinfo,csvfilename):
	interfaceinfo = re.sub('<[^>]*>','',interfaceinfo)
	interfaceinfo = str(interfaceinfo)
	interfaceinfo = interfaceinfo.replace("QoS throughput for interface ethernet1/1","")
	interfaceinfo = interfaceinfo.replace(" node default-group (Qid 0):","")
	interfaceinfo = interfaceinfo.replace("class 4:     ","")
	interfaceinfo = interfaceinfo.replace("kbps","")
	interfaceinfo = interfaceinfo.replace(" ","")
	response_time = strftime("%Y-%m-%d %H:%M:%S")
	stats = str(response_time) + str(interfaceinfo)
	stats = str(stats)
	stats = " ".join(stats.splitlines())
	print stats
	bandwidth_stats_file = csvfilename
	with open(bandwidth_stats_file,'a') as myFile:
		myFile.write(stats + "\n")
		myFile.flush()
		os.fsync(myFile.fileno())
		myFile.close()