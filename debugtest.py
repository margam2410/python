#!/usr/bin/pyhton

def foo():
    return 6

x = foo()
for i in [1, 2, 4, 6, 5]:
    x += i

if x > 23:
    print "Debugging: File1.py, line 11"
    print "Welcome!"      

