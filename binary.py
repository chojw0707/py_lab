#!/usr/bin/python

def b():
	s = input('input binary number: ')
	
	t = int(s , 2)
	o = oct(t)
	h = hex(t)
	

	print('OCT>', o)
	print('DEC>', t)
	print('HEX>', h)
