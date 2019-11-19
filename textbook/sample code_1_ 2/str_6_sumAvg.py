# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:45:12 2018

Get sum and average of a list of numbers
"""

s = input("Enter numbers separated by space: ")

slist = s.split() #里面不填默认以空格分隔
print(slist)

total = 0
for i in slist:
    total = total + int(i)

print("%7s = %d" % ("Total", total))
print("Average = %.2f" % (total/len(slist)))


"""
# Using list comprehension
nlist = [int(x) for x in s.split(' ')]

print("%7s = %d" % ("Total", sum(nlist)))
print("Average = %.2f" % (sum(nlist)/len(nlist)))
"""

