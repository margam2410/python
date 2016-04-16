#!/usr/bin/python
def fibonacci3():
    a,b= 1,1
    while True:
  	yield a
	a,b = b, a+b 

n = 0
for i in fibonacci3():
    if n >= 10:
	break;
    print (i)
    n +=1
