# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:29:24 2018

Find the longest word that has at least 3 counts
"""
#字典排序sorted

word_dict = {'Programming': 13,'Calculus': 2, 'English': 5, 'Discrete Math': 8}
freq_dict = {k:v for k,v in word_dict.items() if v >= 3}
print(freq_dict)
for k,v in freq_dict.items():
    print(k,v)
# sorted() takes a list (or tuple, dict) as an argument and returns a new sorted list.
#l_sorted = sorted(freq_dict.items(), key=lambda x: len(x[0]), reverse=True)
# Sorted by key length   
#字典排序 return的类型是list x是字典的key 按照key长度排序
l_sorted = sorted(freq_dict, key=lambda x: len(x), reverse=True)
l_sorted = sorted(freq_dict, key=len, reverse=True)

# Sorted by key value: dict.get return each key's value 只取了key，输出只有key
# reverse=True 从大到小 False 从小到大 
v_sorted1 = sorted(freq_dict, key=freq_dict.get, reverse=False) 

#取出 .items() 包括key+value 
'''
下面这句命令，lambda是一个隐函数，是固定写法，不要写成别的单词；
x表示列表中的一个元素，在这里，表示一个元组，x只是临时起的一个名字，你可以使用任意的名字；
x[0]表示元组里的第一个元素，当然第二个元素就是x[1]；所以这句命令的意思就是按照列表中第一个元素排序                                                                   
'''
#v_sorted2 = sorted(freq_dict.items(), key=lambda x: x[0], reverse=True) 按照key从大到小排序
v_sorted2 = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True) #按照value从大到小排序

print()
print("Sorted by key length: ")
print(l_sorted)
print()
print("Sorted by key value: ")
print(v_sorted1)
print()
print("Sorted by key value: ")
for k, v in v_sorted2:
  print(k, end=", ")
print()
print('-----------test-----------')
v1 = sorted(freq_dict,key=len,reverse=True) #key从大到小
v2 = sorted(freq_dict.items(),key=lambda x: x[1], reverse=True) #value 从小到大
print(v2)
print(type(v2))
#按key value遍历return的结果
for k,v in v2:
    print(k,v)

