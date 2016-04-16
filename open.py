#!/usr/bin/python

#open a file
fo = open("ma.txt","wb")
print "name of the file :" ,fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
