#!/bin/bash
. ifacename.sh
arp -n -i $name |grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'|uniq 