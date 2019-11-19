# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 23:40:00 2018

"""
#字典的创建/遍历/新增/删除

#创建字典的两种方式
#1 Create a simple dictionary {key1: value1, key2:value2}
dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
print('dict1:',dict1)

#2 Create dictionary using dict()
dict2 = dict(brand="Ford", model="Mustang", year=1964)
## note that keywords are not string literals 不是字串
## note the use of equals  = rather than colon for the assignment
print('dict2:',dict2)

#  通过key获取value
print('key 获取 value:',dict1["year"])

# 通过key更改value
dict2["year"] = 2018
print(dict2)

# 遍历
## get keys
print('----------get keys-----------')
print('----1-----')
for k in dict1:
    print(k)
print('----2-----')
for k in dict1.keys():
    print(k)
    
## get values
print('----------get value----------')
for k in dict1:
    print(dict1[k])
print()
for v in dict1.values():
    print(v)
    
## get key and value
print('----------get k/v------------')
for k, v in dict1.items():
    print(k,v)
print()

# Add new items 字典新增
dict1['color'] = 'red'
print(dict1)

# remove items
#del dict1['color']
dict1.pop('color') # return key's value
print(dict1)

# setdefault: return value of a specific key, otherwise set it
# 如果 "year" 是一個 key, 回傳 dict1["year"], 
# 否則new一个key dict1["year"]=1999, 回傳 1999
x = dict1.setdefault("year", 1999)
print(x)

x = dict1.setdefault("color", "white")
print(x)
print(dict1)

# dir() function returns all properties and methods of the specified object
print(dir(dict1))