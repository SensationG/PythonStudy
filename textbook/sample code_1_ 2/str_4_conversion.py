# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 22:58:43 2018

string conversion
"""

s1 = 'learning pyThon'
print("s1: " + s1)


# s.capitalize(): 字符串的第一个字母变为大写
print("s1.capitalize(): ", end = ' ')
print(s1.capitalize())

# s.title(): 字符串中每个单词的首字母大写
print("s1.title(): ", end = ' ')
print(s1.title())

# s.lower(): 把字串的所有字元變成小寫
print("s1.lower(): ", end = ' ')
print(s1.lower())

# s.upper(): 把字串的所有字元變成大寫
print("s1.upper(): ", end = ' ')
print(s1.upper())

# s.swapcase(): 把字串的所有字元大寫-> 小寫， 小寫 -> 大寫
print("s1.swapcase(): ", end = ' ')
print(s1.swapcase())

# s.replace(old, new): 替换字符串中的内容
print("s1.replace(' ', '-'): ", end = ' ')
print(s1.replace(' ', '-')) 