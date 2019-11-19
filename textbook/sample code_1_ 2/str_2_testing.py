# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 22:58:43 2018

Testing String
"""

s1 = 'LearningPython'
s2 = '12345678'


# s.isalnum(): 字母 + 數字
print(s1.isalnum())

# s.isalpha(): 字母
print(s1.isalpha())

# s.isdigit(): 數字
print(s1.isdigit())
print(s2.isdigit())

# s.islower(): 小寫
print(s1.islower())

# s.isupper(): 大寫
print(s1.isupper())

# # s.upper(): 變成大寫
print(s1.upper().isupper())