# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 22:58:43 2018

String as an array
"""

s1 = str()

s2 = ''

s3 = 'This is s3'

s4 = str("Learning Python")

print("s4: " + s4)

# 字符串的长度
print("Length of s4: ", len(s4))

# 打印字符串的首个字母
print("s4[0]: " + s4[0])

print("s4[1:5]: " + s4[1:5]) # 字符串起始1-4位字母

print("s4[-1]: " + s4[-1])  # 反过来打印 末尾开始第0位

print("s4[1:]: " +s4[1:]) # starts with index 1

print("s4[:2]: " +s4[:2]) # 第二位结束（不包括第二位）
    
# String adding and multiplcation
print("s4 + ' ' + s3 = " + s4 + ' ' + s3)

print("s4 * 2 = " + s4 * 2) #字符串乘n = 重复n遍

# Loop through string
for c in s4:
    print(c, end = ' ')
print()
