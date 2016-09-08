#!/bin/bash
addr=`cat /sys/class/net/$name/address | sed s/://g|tail -c 7` #getting the last 6 numbers from the hwaddress
xh=`echo $addr |cut -c 1-2` 
x=`expr $((16#$xh))` #converting to decimal
yh=`echo $addr |cut -c 3-4`
y=`expr $((16#$yh))` #converting to decimal
zh=`echo $addr |cut -c 5-6`
z=`expr $((16#$zh))` #converting to decimal
ip=`expr 10.$x.$y.$z` #appending the converted bits 
