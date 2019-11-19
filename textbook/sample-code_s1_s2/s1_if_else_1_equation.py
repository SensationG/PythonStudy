# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

num = input('Enter a, b, c: ')
print(type(num))

a, b, c = eval(input('Enter a, b, c: ')) 

d = b**2  - 4 * a * c

if d > 0:
    print("d = %d, Has two solutions" % (d))
elif d == 0:
    print('d = %d, Has one solution' % (d))
else:
    print('d = %d, Has no "solution"' % (d))
print('Over')