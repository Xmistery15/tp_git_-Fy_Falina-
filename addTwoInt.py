#!/usr/bin/env python

import sys

print(sys.argv)

def add(a,b):
	return a+b

#main qui va tester la fonction

x=int(sys.argv[1])
y=int(sys.argv[2])

print(add(x,y))

