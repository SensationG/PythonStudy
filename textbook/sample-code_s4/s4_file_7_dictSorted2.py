# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:17:55 2018

"""
from collections import Counter
from heapq import nlargest
#heapq 模块有两个函数：nlargest() 和 nsmallest()

#------------------查找字典里value最大/最小的n个元素/heapq模块 Count模块-----------------

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(my_dict)
# dict.get() returns the value for the given key, if present in the dictionary. 
# otherwise, it will return None

# 1: Using sorted 都是对value进行排序
print('------对value进行排序---------')
#按value排序
sorted1 = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted1[0:3])

# my_dict[x] x是my_dict，按value进行排序 输出key
sorted2 = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)
print(sorted2[0:3])

# 按value进行排序 输出key
sorted3 = sorted(my_dict, key=my_dict.get, reverse=True)
print(sorted3[0:3])

# 2: Using heapq.nlargest
print('--------nlargest模块 查找最大/最小的N个元素---------')
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest) 

# 3: Using collections.Counter()
print('---------Count计数函数---------------------')
counter = Counter(my_dict) #对字典按value值进行排序
print(counter)
highs = counter.most_common(3) #前三个组成的列表
print(type(highs)) 
print([x[0] for x in highs]) #只打印key

# Count也可以统计字符串每个单字重复的次数
c = Counter('hello,world')
print(c)
