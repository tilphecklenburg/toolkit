from panosapifunctions import genapikey, getbandwidth, savebandwidthtocsv
from twisted.internet import task
from twisted.internet import reactor

apikey = genapikey("172.23.96.7","adm-longview","1nPr0gr3ss!")

def infogather():
	interfaceinfo = getbandwidth("172.23.96.7",apikey)
	savebandwidthtocsv(interfaceinfo,"NPY - results.csv")
	print "gathering interface data"
	pass
	
timeout = 60.0 # Sixty seconds

l = task.LoopingCall(infogather)
l.start(timeout) # call every sixty seconds

reactor.run()