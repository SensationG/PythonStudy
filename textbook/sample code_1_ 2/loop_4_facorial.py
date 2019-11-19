# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:45:22 2018

Factorial
"""
n = eval(input('Enter a two-digit number: '))

for i in range(1, n+1):
    factor = 1
    for j in range(1, i+1):
        factor *= j
    print('#%2d! = %d' % (i, factor))
