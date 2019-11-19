# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:28:09 2018

sum of integers 1 .. 100
"""
i = 1
total = 0

while i <= 100:
    total += i
    i += 1
print('total by while loop = ',  total)


total = 0

# for i in range(start, end, step)
for i in range(1, 101):
    total += i
    #print(i)
    i += 1
    
print('total by for loop   = ',  total)

