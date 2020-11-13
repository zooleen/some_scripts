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
