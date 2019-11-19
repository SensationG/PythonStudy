# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:34:37 2018

"""
# 9 * 9 Multiplcation table

for x in range(1, 10):
    for y in range(1, 10):
        print('%d*%d=%2d' % (x, y, x*y))
    print()

for x in range(1, 10):
    for y in range(1, 10):
        print('%d*%d=%2d ' % (y, x, x*y), end=' ')
        print()
    print()
    