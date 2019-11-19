# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 22:58:43 2018

substring
"""

s1 = 'LearningPython'
s2 = '12345678'

print("s1: " + s1)
print("s2: " + s2)

# s.endswith(substring): 以 substring 結束
print("s1.endswith('thon'): ", end = ' ')
print(s1.endswith('thon'))

# s.startswith(substring): 以 substring 開始
print("s1.startswith('learn'): ", end = ' ')
print(s1.startswith('learn'))

# s.find(substring): 找到第一個 substring 的  index
print("s1.find('n'): ", end = ' ')
print(s1.find('n'))

# s.rfind(substring): 找到最後一個 substring 的  index
print("s1.rfind('n'): ", end = ' ')
print(s1.rfind('n'))

# s.count(substring): 找到 substring 出現的次數
print("s1.count('n') ", end = ' ')
print(s1.count('n'))