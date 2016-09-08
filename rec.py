import socket
import sys
import os
import subprocess,threading
import time
pwd = "1202"

def SendHostName():
	#Sends its accountname to other devices when requested through port 7777
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#hostname = socket.gethostname()
	server_address = ('10.39.246.0', 7777)
	username = subprocess.check_output('whoami', shell=True).decode()
	sock.bind(server_address)
	sock.listen(5)
	n  = len(username)
	username = "phoenix"#str(username[0:n-1])
	while True:
	    # Wait for a connection
	    #print("waiting for a connection")
		connection, client_address = sock.accept()
		#request = connection.recv(1024)
	    #if request == "host":
		data = str(username)+","+str(pwd)
		# print(data)
		connection.send(bytes(data, 'UTF-8'))
SendHostName()
