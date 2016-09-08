import subprocess,threading


print("Hi , do you want to ")
print("1.Create")
print("2.Connect")
x=int(input())
if x==1:
	print("You have selected to Create")
	subprocess.call('./assign.sh',shell=True)
else:
	print("You have selected to Connect")
	subprocess.call('./assign.sh',shell=True)


#subprocess.call('sudo service network-manager start',shell=True)
