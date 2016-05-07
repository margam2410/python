#!bin/usr/python
import re
with open('info.txt', 'r') as fname:
#with fname.open('info.txt','r') as fname:
    data=fname.readline()
    m=re.search("(?P<first_name>\w+):(?P<last_name>\w+)", data)
   # print m.group('first_name'),'[',m.group('last_name'),']'
    print m.group('first_name') ,'[',m.group('last_name'),']'
fname.close()
