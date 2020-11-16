#!/usr/bin/python3
#
# This script examing argument host for redirecting to ezaem

from sys import argv
from sys import exit
from os import popen
import re

scriptName, targetHost = argv

ext = popen("curl -Ls -o /dev/null -w %{url_effective} " + targetHost + "/click/1/1")
# Amazing code <3
for i in ext:
    myStr = i
    break

print(myStr)

if (re.search('ezaem', myStr) == None):
    exit(1)
else:
    exit(0)
