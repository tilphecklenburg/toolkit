import paramiko
import time
hostname = ""
remote_conn_pre = ''
remote_conn = '' 

#can be used to start up a paramiko ssh session with a device


def sshconnect(ip, username, password):
	global remote_conn_pre
	global remote_conn
	#initialize paramiko SSH client
	remote_conn_pre = paramiko.SSHClient() 
	#------------------------------------------------------------------
	#if the SSH key presented by the server is not yet known, ignore warnings and add it to client 
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
	#------------------------------------------------------------------
	#open connection to the device
	remote_conn_pre.connect(ip,username=username,password=password,look_for_keys=False,allow_agent=False)
	#------------------------------------------------------------------
	#invoke a shell object to send commands once SSH session is established
	remote_conn = remote_conn_pre.invoke_shell()
	return remote_conn
	#------------------------------------------------------------------
#------------------------------------------------------------------

#can be used to gather the cisco device's hostname


def getciscohostname(ip, username, password):
	global hostname
	global remote_conn_pre
	global remote_conn
	#initialize paramiko SSH client
	remote_conn_pre = paramiko.SSHClient() 
	#------------------------------------------------------------------
	#if the SSH key presented by the server is not yet known, ignore warnings and add it to client 
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
	#------------------------------------------------------------------
	#open connection to the device
	remote_conn_pre.connect(ip,username=username,password=password,look_for_keys=False,allow_agent=False)
	#------------------------------------------------------------------
	#invoke a shell object to send commands once SSH session is established
	remote_conn = remote_conn_pre.invoke_shell() 
	#------------------------------------------------------------------
    #gathering hostname from first few bits of SSH session
	hostname = remote_conn.recv(5000)
	hostname = hostname.replace("#","")
	hostname = hostname.replace(">","")
	hostname = hostname.replace("\n","")
	#------------------------------------------------------------------
#------------------------------------------------------------------

#gather cisco IOS based device's running config and return it in a text file


def getiosconf(ip, username, enablepw, password):
	global hostname
	global remote_conn_pre
	global remote_conn
	try:
		#initialize paramiko SSH client
		remote_conn_pre = paramiko.SSHClient() 
		#------------------------------------------------------------------
		#if the SSH key presented by the server is not yet known, ignore warnings and add it to client 
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
		#------------------------------------------------------------------
		#open connection to the device
		remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
		#------------------------------------------------------------------
		#invoke a shell object to send commands once SSH session is established
		remote_conn = remote_conn_pre.invoke_shell() 
		#------------------------------------------------------------------
		#gathering hostname from first few bits of SSH session
		hostname = remote_conn.recv(5000)
		if ">" in hostname:
			remote_conn.send("en\n")
			time.sleep(1)
			remote_conn.send(enablepw + "\n")
			time.sleep(1)
		hostname = hostname.replace("#","")
		hostname = hostname.replace(">","")
		hostname = hostname.replace("\n","")
		hostname = hostname.replace("\r","")
		#------------------------------------------------------------------
		#Create config text file to add output to
		config = open("%s - running config.txt" % hostname, "a")
		remote_conn.send("term len 0\n")
		time.sleep(2)
		cleanup = remote_conn.recv(5000)
		remote_conn.send("show run\n")
		time.sleep(10)
		runningconfig = remote_conn.recv(1000000)
		config.write(runningconfig)
		config.close()
		return True
		#------------------------------------------------------------------
	except:
		return False
