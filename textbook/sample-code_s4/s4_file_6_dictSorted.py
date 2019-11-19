# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:29:24 2018

Find the longest word that has at least 3 counts
"""
#----------------字典排序--------------------

word_dict = {'Programming': 13,'Calculus': 2, 'English': 5, 'Discrete Math': 8}
freq_dict = {k:v for k,v in word_dict.items() if v >= 3} 
print(freq_dict)

# sorted() takes a list (or tuple, dict) as an argument and returns a new sorted list.
#按value长度排序
#l_sorted = sorted(freq_dict.items(), key=lambda x: len(x[0]), reverse=True)

# Sorted by key length
# 按key长度排序：即单词长度
l_sorted = sorted(freq_dict, key=lambda x: len(x), reverse=True)

# Sorted by key value
# 按value排序
v_sorted = sorted(freq_dict, key=freq_dict.get, reverse=True) # value-based sorting

print()
print("Sorted by key length: ")
print(l_sorted)
print()
print("Sorted by key value: ")
print(v_sorted)

