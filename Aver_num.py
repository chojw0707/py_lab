#!/usr/bin/python

num = input('how many numbers?')

n = int(num)

a = []

for i in range(n):
		
	a.append(int(input()))
	

sum=0

for i in range(len(a)):
	sum = sum + a[i]
average  = sum / len(a)

print(average)
