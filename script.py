#!/usr/bin/python3
# This script reads arguments from a command-line.
# Also it uses regular experssions for a extract IP
# address from a string.
# Maked for one guy from tg:@srv_admins
# Usage: ./script.py <hostame>
# For local usage only
# Copyright Ivan Doobro 2020

from sys import argv

i, ihost = argv

import os
import re
vid = os.popen("host " + ihost)
re_dns = re.compile(r"([\d]+)\.([\d]+)\.([\d]+)\.([\d]+)")
for line in vid.readlines():
  hst=re_dns.search(line)
  if (hst != None):
    break
host=hst.group(0)
if (host != None):
    print(ihost + " host adress is " + host)
else:
    print("Unknown host.")
