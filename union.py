#!/usr/bin/python

def c():
	a = []
	b = []
	print('input 1st list: ')
	for i in range(1):
		k = input()
		a.append(k)
	
	map(int , a)
	al = " , ".join(a)
	

	print('input 2nd list: ')
	for i in range(1):
		k = input()
		b.append(k)
	map(int , b)
		
	bl = " , ".join(b)

	set1 = set(al)
	set2 = set(bl)
	
	print('union' , set1 | set2)
	print('intersection' , set1 & set2)

	

	
	
