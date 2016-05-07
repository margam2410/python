#!/usr/bin/python
import re

line = "mahesh are margam"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.M)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"
