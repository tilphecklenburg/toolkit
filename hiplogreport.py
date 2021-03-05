import xml.etree.ElementTree as ET
import csv
import datetime
import panosapifunctions
import requests
from time import sleep

#-------------------------create API key-------------------------------------------------------------------------
apikey = panosapifunctions.genapikey('10.200.5.10', 'admin', 'wirefire911')
print('got api key: %s' % str(apikey))

#-------------------------run search and get job ID--------------------------------------------------------------
jobidquerystring = 'https://10.200.5.10/api/?key=' + apikey + '&type=log&log-type=hipmatch&nlogs=200&query=' + "( user.src eq 'philip.tecklenburg@wirefire.ca')"
print(jobidquerystring)

response = requests.get(jobidquerystring, verify=False)
jobidstring = str(response.text)
jobidxmlfile = open('jobidxml', 'w')
jobidxmlfile.write(jobidstring)
jobidxmlfile.close()
tree = ET.parse("jobidxml")
root = tree.getroot()
for child in root:
    if child.tag == 'result':
        jobid = child.find('job').text
print('job id: %s' % jobid)

print('sleeping for 10 seconds to let job do its thing')
sleep(10)

#-------------------------get logs xml---------------------------------------------------------------------------
logquerystring = 'https://10.200.5.10/api/?key=' + apikey + '&type=log&action=get&job-id=' + jobid
response = requests.get(logquerystring, verify=False)
logs_string = str(response.text)
logsxmlfile = open('logsxml', 'w')
logsxmlfile.write(logs_string)
logsxmlfile.close()