from sshfunctions import getiosconf

def gatherconfig(hostlist):
	for ip in hostlist:
		success = getiosconf(ip,"mxadmin","optima","Tobag0")
		if success == False:
			success = getiosconf(ip,"netmin","optima","d3nv3r!")
			if success == False:
				success = getiosconf(ip,"mxadmin","optima","Meth@n0l")
				if success == False:
					success = getiosconf(ip,"Admin","optima","P455w0rd!")

hostlist = open("hostlist.txt","r+")
hostlist = hostlist.read()
hostlist = hostlist.split("\n")

gatherconfig(hostlist)