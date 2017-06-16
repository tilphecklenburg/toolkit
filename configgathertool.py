from sshfunctions import getiosconf

def gatherconfig(hostlist):
	for ip in hostlist:
		success = getiosconf(ip,"","","")
		if success == False:
			success = getiosconf(ip,ip,"","","")
			if success == False:
				success = getiosconf(ip,ip,"","","")
				if success == False:
					success = getiosconf(ip,ip,"","","")

hostlist = open("hostlist.txt","r+")
hostlist = hostlist.read()
hostlist = hostlist.split("\n")

gatherconfig(hostlist)
