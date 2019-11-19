# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 22:58:43 2018

String as an array
"""

s1 = str()

s2 = ''

s3 = 'This is s3'

s4 = str("程式設計")

print("s4: " + s4)

# Length of string
print("Length of s4: ", len(s4))

# Access string element
print("s4[1]: " + s4[1])

print("s4[1:5]: " + s4[1:5]) # start..end-1

print("s4[-1]: " + s4[-1])  # index = len(s4) + (-1)

print("s4[1:]: " + s4[1:]) # starts with index 1

print("s4[:2]: " + s4[:2]) # ends with index 2-1

# String adding and multiplcation
print("s4 + ' ' + s3 = " + s4 + ' ' + s3)

print("s4 * 2 = " + s4 * 2)

# Loop through string
for c in s4:
    print(c, end = ' ')