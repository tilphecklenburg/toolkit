from snmp_helper import snmp_extract, snmp_get_oid
uptime = int()

def snmp_getuptime(ip,communitystring,port):
	global uptime
	device = (ip,communitystring,port)
	uptime = int(snmp_extract(snmp_get_oid(device,oid=".1.3.6.1.2.1.1.3.0",display_errors=True))) / 60480000
	return uptime
