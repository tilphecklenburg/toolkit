from fmcapifunctions import getdomainuuid
from fmcapifunctions import postnewobject
from fmcapifunctions import getauthtoken
print """

Thank you for using the FMC network object import tool, 
and please note the following:

No support will be provided for this script, 
it is presented as-is and features may or may not be added in future versions.
The creator is not responsible for any downtime incurred or misconfiguration 
applied on customer systems; development, production or otherwise.

Server certificate verification is DISABLED on this script. 

If server verification is desired, an alternate script version can be used, but will not be supported.

"""

username = raw_input("Enter FMC username>>> ")
password = raw_input("Enter FMC password>>> ")
filename = raw_input("""

Enter name of CSV file to import objects from, should be in the same dir as this EXE,
and please note the required format:
" objectname,object value (the address corresponding to the object),a short description for object, and object type (host, network, etc.) " 

Please do not include headers in the CSV file, commas to delimit each column are sufficient as contents of each column is assumed.

CSV File>>>""")

server = raw_input("""

Enter host name or IP of FMC:

FMC Host name or IP>>>""")

domainuuid = getdomainuuid(server,username,password)
authtoken = getauthtoken(server,username,password)
csvfile = open(filename,"r+")
print domainuuid
rawtext = csvfile.read()

rawtext = rawtext.split("\n")

log = open("log.txt","a")

for line in rawtext:
	line = line.split(",")
	if postnewobject(server,domainuuid,authtoken,str(line[0]),str(line[1]),str(line[2]),str(line[3])) == True:
		log.write("%s imported successfully" % str(line[0]) + "\n")
	else:
		log.write("%s import failed" % str(line[0]) + "\n")

log.close
	