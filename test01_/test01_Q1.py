# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:11:34 2019

@author: hhw
"""

i = input('Please enter a number: ')
sum=int(i)
a=1
s=sum-1
s1=0
a1=1
for t in range(sum-1):
    a1=a1+2

for e in range(sum):
    print(" "*s1,end="")
    print('*'*a1)
    a1=a1-2
    s1=s1+1 
    
for i in range(sum):
    print(" "*s,end="")
    print('*'*a)
    a=a+2
    s=s-1

