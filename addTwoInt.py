#!/usr/bin/env python

import sys

print(sys.argv)

def add(a,b):
	return a+b

#tester si le nombre d'argument est correct
#et afficher un message d'erreur sinon
nbr_arg=len(sys.argv)-1
if (nbr_arg != 2):
	print("Assurez-vous de mettre en argument les 2  chiffres à ajouter")

#main qui va tester la fonction

x=int(sys.argv[1])
y=int(sys.argv[2])

print(add(x,y))

