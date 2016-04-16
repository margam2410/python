#!/usr/bin/python

#open a file

fo = open("ma.txt","r+")
str = fo.read(22);
print "Read String is : ", str
# Close opend file
fo.close()
