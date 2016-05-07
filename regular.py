import re
import os 
import urllib2
with open('mahi.txt', 'r') as fname:
    #m=re.search("(?P<first_name>\S+):(?P<last_name>\S+)", fname.read())
    #m=re.search("(?P<first_name>\w+):(?P<last_name>\w+)", fname.read())
    #m=re.search("(?P<first_name>\w+):(?P<last_name>\w+)", fname.readlines())
    #data=fname.read()
    #data=fname.readline()
    data=fname.readlines()
    m=re.search("(?P<first_name>\w+):(?P<last_name>\w+)", data)
    #m=re.search("(?P<first_name>\w+):(?P<last_name>\w+)", fname.readline())
    print m.group('data.first_name'),'[',m.group('data.last_name'),']'
    print m.group('data.first_name'),'[',m.group('data.last_name'),']'
    #print m.group('first_name'),'[',m.group('last_name'),']'
    #print m.group('first_name'),'[',m.group('last_name'),']'
fname.close()
