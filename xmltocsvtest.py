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
jobidquerystring = 'https://10.200.5.10/api/?key=' + apikey + '&type=log&log-type=traffic&nlogs=5000&query=' + "(rule eq 'intrazone-default')"
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

#-------------------------parse logs xml and convert to CSV------------------------------------------------------
tree = ET.parse("logsxml")
root = tree.getroot()
#t = (datetime.datetime.now()).strftime('%Y-%m-%d')
#trafficlogcsv = open('trafficlogcsv  - %s.csv' % t, 'w', newline='')
trafficlogcsv = open('trafficlogcsv.csv', 'a+', newline='')
csvwriter = csv.writer(trafficlogcsv)
count = 0
for child in root:
    if child.tag == 'result':
        for entry in child:
            if entry.tag == 'log':
                for element in entry:
                    if element.tag == 'logs':
                        for log in element:
                            csventry = []
                            sourcezone = log.find('from').text
                            csventry.append(sourcezone)
                            destzone = log.find('to').text
                            csventry.append(destzone)
                            sourceIP = log.find('src').text
                            csventry.append(sourceIP)
                            destIP = log.find('dst').text
                            csventry.append(destIP)
                            sourceport = log.find('sport').text
                            csventry.append(sourceport)
                            destport = log.find('dport').text
                            csventry.append(destport)
                            protocol = log.find('proto').text
                            csventry.append(protocol)
                            app = log.find('app').text
                            csventry.append(app)
                            action = log.find('action').text
                            csventry.append(action)
                            rule = log.find('rule').text
                            csventry.append(rule)
                            csvwriter.writerow(csventry)

trafficlogcsv.close()
