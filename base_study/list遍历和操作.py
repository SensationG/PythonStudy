# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:14:48 2019

@author: hhw
"""

#1 遍历容器/字符串 操作都通用
'''
for 变数 in 容器
    程式区块
'''
lst = ['apple','banana','cocount','orange']
my_str = 'This is Python'

    #方法1
for i in range(len(my_str)):
    print(my_str[i],end=' ') #end=' ' 使得print不换行
  
print()
    #方法2
for i in my_str:
    print(i,end=' ')
    
print()
    #方法3 可输出index索引值 [:2]标识输出第0-1位
for i,x in enumerate(my_str[:2]):
    print(i,x)

#判断是否在list/str中 in/not in
if 'apple' in lst:
    print('true')
    
#2 更新list
list = []
list.append('Google')
list.append('yahoo')
print(list)

#3 删除list 
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2] #del删除指定list

list1.append('google')
list1.remove('google') #remove 删除指定元素
print(list1)

a=list1.pop() #pop 若不指定元素位置 则默认删除-1位置元素 返回值是删除的元素
print(a)
print(list1)


#4 两个list操作
print(list1+list)#两个list相加

#5 list长度
print(len(list1))

#6 list某个元素出现的个数
list3 = [1,2,3,1,3,1,3]
print(type(list3))

#7 找出list某个元素的第一个index
print(list3.index(3)) # 数字3 第一次出现的位置是2

#7 插入元素到xx位置
list3.insert(1,'this')
print(list3)

#8 移除列表中某个值的第一个匹配项
list3.remove('this')
print(list3)

#9 排序
list3.sort() #小到大
print(list3)
list3.sort(reverse=True) #大到小
print(list3)


