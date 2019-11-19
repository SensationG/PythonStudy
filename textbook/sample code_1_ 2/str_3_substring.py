# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 22:58:43 2018

substring
"""

s1 = 'LearningPython'
s2 = '12345678'

print("s1: " + s1)
print("s2: " + s2)

# s.endswith(substring): 判断是否以 substring 結束
print("s1.endswith:('thon') ", end = ' ')
print(s1.endswith('thon')) #判断是否以 substring 結束

# s.startswith(substring): 以 Learn 開始
print("s1.startswith('Learn'): ", end = ' ')
print(s1.startswith('Learn')) 

# s.find(substring): #找到s1中首个n的index
print("s1.find('n'): ", end = ' ')
print(s1.find('n')) #找到s1中首个n的index

# s.rfind(substring): 找到s1中最后一个n的index
print("s1.rfind('n'): ", end = ' ')
print(s1.rfind('n')) 

# s.count(substring): 找到s1中n出现的次数
print("s1.count('n') ", end = ' ')
print(s1.count('n'))