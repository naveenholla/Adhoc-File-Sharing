#!/bin/bash
name=`sudo ifconfig | cut -c 1-8 |grep ^w|tr -d '\n'` #getting the name of the wireless interface
name=`echo $name|tr -d '\n'` #traucating the non-printable chars in interface name