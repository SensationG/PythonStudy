# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:45:22 2018

Factoria: Using function
"""

def factorial(k):
    for i in range(1, k+1):
        result = 1
        for j in range(1, i+1):
            result *= j
        print('#%2d! = %d' % (i, result))

def main():
    n = eval(input('Enter a two-digit number: '))
    factorial(n)

main()
