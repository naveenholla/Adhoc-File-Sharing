#!/bin/bash
. ifacename.sh
. getip.sh
sudo service network-manager stop #stoping the network manager
sudo ip link set $name down #getting the link down
wifiname="Trojans"
sudo iwconfig $name mode ad-hoc essid $wifiname key 1234567890 #creating adhoc network 
sudo ip link set $name up
sudo ifconfig  $name $ip/8 #assigning ip using ifconfig
python3 rec.py & >/dev/null
python3 ShareIt.py
