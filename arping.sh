#!/bin/bash
. ifacename.sh
. getip.sh
sudo arping -A -c 5 -I $name  $ip  > /dev/null