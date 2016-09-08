import socket
import sys
import os
import subprocess,threading
import time

l = {}
pwd = ""

def broadcast():
    subprocess.call(['./arping.sh ','&'],shell=True)
    threading.Timer(1, broadcast).start()

def getips():
	j = 1
	output = subprocess.check_output("./arptable.sh", shell=True)
	time.sleep(2)
	#print (output)
	x=str(output).split('\\n')
	# print(x)
	if len(x) >0:
		x.pop()
		temp=x[0]
		x[0]=temp[2:]
		for i in x:
			l[j]=i
			j=j+1
	# print(l)


def SendHostName():
	#Sends its accountname to other devices when requested through port 7777
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	hostname = socket.gethostname()
	server_address = (hostname, 7777)
	username = subprocess.check_output('whoami', shell=True).decode()
	sock.bind(server_address)
	sock.listen(10)
	n  = len(username)
	username = str(username[0:n-1])
	while True:
	    # Wait for a connection
	    #print("waiting for a connection")
		connection, client_address = sock.accept()
		#request = connection.recv(1024)
	    #if request == "host":
		data = str(username)+","+str(pwd)
		#print(data)
		connection.send(bytes(data, 'UTF-8'))	
	    


def sendUnicast():
	#displayDevices();
	rec = (input("\nSelect the user to send\n"))
	while int(rec) > len(l):
		rec = input("Please enter valid Input\n")	
	filename = input("Enter the filename\n")
	host = findHostDetails(int(rec))
	# os.system(sudo su )
	rec = int(rec)
	un = host[0]
	pd = host[1]
	cmd = "sshpass -p "+"'"+str(pd)+"'" +" scp "+ "/home/phoenix/" + str(filename) +" " + str(un) +"@"+str(l[rec]) + ":/home/"+str(un)+"/SharedFolder"
	status = ValidateFile(filename)
	if status == True:
		cmdSuccess = os.system(cmd)
		#print(cmdSuccess)
		#print(cmd)
		if cmdSuccess == 0:
			print("File "+filename +" transfered Succesfully\n")
			ShowOptions()
		else:
			print("Operation Failed\n")
			ShowOptions()
	else:
		print("File Does Not Exists..please try again\n")
		ShowOptions()


def sendMulticast():
	#displayDevices()
	count = 0
	rec = input("\nSelect the users to send(Use ',' to seperate users)")
	rec = str(rec).split(",")
	filename = input("Enter the filename\n")
	status = ValidateFile(filename)
	if status == True:
		for i in rec:
			host = findHostDetails(int(i))
			#print(str(host))
			i = int(i)
			un = host[0]
			pd = host[1]
			cmd = "sshpass -p "+"'"+str(pd)+"'" +" scp "+ "/home/ubuntu/" + str(filename) +" " + str(un) +"@"+str(l[i]) + ":/home/"+str(un)+"/SharedFolder > out.log"
			#cmd = "scp "+ filename + " " + str(host) +"@"+l[rec] + ":/SharedFolder"
			print(cmd)
			cmdSuccess = os.system(cmd)
			time.sleep(5)
			if cmdSuccess == 0:
				#print("File transfered Succesfully\n")
				count = count +1
			else:
				print("Operation Failed.... Reciever--->"+str(l[i])+"\n")
		if count == len(rec):
			print("File Transfered to all "+ str(count) +" devices...Successfully\n")
			ShowOptions()
		else:
			print("File transefed to "+str(count)+" nodes only\n")
			ShowOptions()
	else:
		print("File Does Not Exists\n")
		ShowOptions()


def displayDevices():
	print("Devices present in the Network\n")
	for i in l:
		print(str(i)+". " + str(l[i])+"\n")
	ShowOptions()

def ValidateFile(fn):
	return os.path.exists(str(fn))

def findHostDetails(i):
	#Asks for the hostname of the other device when required
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#print(l[i]) Valid
	i = int(i)
	server_address = (l[i],7777)
	#server_address = (socket.gethostname(),7777)
	sock.connect(server_address)
	#sock.send(str("host"))
	hostname = sock.recv(1024).decode().split(",")
	un = hostname[0]
	pd = hostname[1]
	#print(un+" "+pd)
	return hostname

def Disconnect():
	print("Disconnecting...\n")
	exit(0)

def ShowOptions():
    ch = input("1. Check Devices Connected\n2. Send File(Unicast)\n3. Send File(Multicast)\n4. Quit\n")
    if ch == '1':
        displayDevices()
    if ch == '2':
        sendUnicast()
    if ch == '3':
        sendMulticast()
    if ch == '4':
        Disconnect()
    


def askPassword():
    os.system("sudo -k")
    pwd = input("Please Enter your system password\n-->")
    askpwd = "echo "+ pwd +" | sudo -S -v > tmp"
    val = os.system(str(askpwd))
    # subprocess.call('exit',shell=True)
    print(subprocess.check_output('whoami',shell=True))
    print("\n")
    if val == 0:
        #os.system("sudo -k")
        print("Please choose your options")	
        ShowOptions()
    else:
        print("Wrong Password...\n")
        askPassword()



if __name__ == "__main__":
	broadcast()
	getips()
	#SendHostName()
	askPassword()
	#subprocess.call(['python3','recieve.py ',pwd],shell=True)
    #ShowOptions()
    

    


#main()


