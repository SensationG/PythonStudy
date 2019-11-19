# -*- coding: utf-8 -*-
"""
Spyder Editor

multiple typed inputs
"""

a, b = eval(input('Enter two numbers (seperated by comma): ')) 

print(type(a), type(b))

a, s = input('Enter a,s: ').split(',')

if type(s) != type(a):
    print("You have entered Different typed data")
else:
    print(type(a), type(s))
    print("You have entered SAME typed data")