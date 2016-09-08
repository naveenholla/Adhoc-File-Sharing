#!/bin/bash
. ifacename.sh
cd proc/sys/net/ipv4/conf/$name/
cat arp_accept
#cat proc/sys/net/ipv4/conf/$name/arp_accept

