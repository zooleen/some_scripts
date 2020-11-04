#!/bin/bash

if [ -z "$1" ]
    then
        echo "Argument is needed! On input we must have a list of IP addresses (one line for one address)"
        exit 1
fi

while IFS= read -r ip_address
do
    mkdir -p $ip_address/`date -I`
    wget http://$CAM_LOGIN:$CAM_PASSWD@$ip_address -O $ip_address/`date -I`/`date +%T`.jpg
    sleep 1
done < $1
