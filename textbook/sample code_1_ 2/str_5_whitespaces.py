# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 22:58:43 2018

Removing whitespace
"""
# s1 左右各有三個空白
s1 = '   learning  python   '
print("s1: " + s1 +  '...')

# s.lstrip(): 刪除字串左側空白後回傳
print("s1.lstrip():", end = '')
print(s1.lstrip() + '...')

# s.rstrip(): 刪除字串右側空白後回傳
print("s1.rstrip():", end = '')
print(s1.rstrip() + '...')

# s.strip(): 刪除字串兩側空白後回傳
print("s1.strip():", end = '')
print(s1.strip() + '...')

# s.split(): 切割字串
print("s1.split(' '):", end = '')
l = s1.split(' ')  # 以空格切割, 回傳 list
print(l)

# list.split(' ') == list.split() ?
l1 = s1.strip().split(' ')
l2 = s1.strip().split()
print(l1 == l2)

#print("s1.strip().split(' '):" , l1)
#print("s1.strip().split():" , l2)



