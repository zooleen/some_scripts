#!/usr/bin/python3
#
# This script examing <host> from first argument
# for redirecting to a link that include <expression>
# from second argument.
#
# Returns 0 if ok, else return 1.
#
# Usage: ./check_redirect.py <some_host> <expression>
#
# Ivan Doobro 2020

from sys import argv
from sys import exit
from os import popen
import re

scriptName, targetHost, expression = argv

ext = popen("curl -Ls -o /dev/null -w %{url_effective} " + targetHost + "/click/1/1")
# Amazing code <3
for i in ext:
    myStr = i
    break

if (re.search(expression, myStr) == None):
    exit(1)
else:
    exit(0)
