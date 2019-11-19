# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:42:46 2018

大樂透電腦選號： 6個 1-49 的亂數
"""
import random

# Create lotto numbers first try   
lotto = []
for i in range(1, 7): # 1 <= i < 7
    rn = random.randint(1, 49) # 1 <= N <= 49.
    lotto.append(rn)
    
print('The Lotto numbers are:')
for l in lotto:
    print('%3d' % (l), end = ' ')

# Create lotto numbers without duplicates   
lotto = []
n = 1
while n <= 6:
    rn = random.randint(1, 49)
    if rn not in lotto:
        lotto.append(rn)
        n += 1

print()    
print('The Lotto numbers (without duplcates) are:')
for l in lotto:
    print('%3d' % (l), end = ' ')

print()