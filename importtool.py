from fmcapifunctions import getdomainuuid
from fmcapifunctions import postnewhostobject
domainuuid = getdomainuuid("https://192.168.1.65","admin","Imth30n3!")
csvfile = open("hoststoimport.csv","r+")

rawtext = csvfile.read()

rawtext = rawtext.split("\n")

for line in rawtext:
	line = line.split(",")
	postnewhostobject("https://192.168.1.65",domainuuid,"admin","Imth30n3!",str(line[0]),str(line[1]),str(line[2]))
	