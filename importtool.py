from fmcapifunctions import getdomainuuid
from fmcapifunctions import postnewobject

username = raw_input("Enter FMC username>>> ")
password = raw_input("Enter FMC password>>> ")
filename = raw_input("""

Enter name of CSV file to import objects from, and please note the required format:
objectname,object value (the address corresponding to the object),a short description for object, and object type (host, network, etc.) 

>>>
""")

server = raw_input("""

Enter URL to server in the following format:

https://<servername>

>>>
""")
domainuuid = getdomainuuid(server,username,password)
csvfile = open(filename,"r+")

rawtext = csvfile.read()

rawtext = rawtext.split("\n")

for line in rawtext:
	line = line.split(",")
	postnewobject(server,domainuuid,username,password,str(line[0]),str(line[1]),str(line[2]),str(line[3]))
	