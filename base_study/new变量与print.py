# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:48:06 2019

@author: hhw
"""
#new 变量
a = 100 #创建int型变量
b = 100.0   #创建float型变量
c = 'haha'  #创建str型变量
d = [] #创建空list
e = ['a','b','c'] #创建list 使用append添加元素
dict = {} #创建字典

print(type(dict)) #检查变量类型

#字符串操输出 / 同样适用list表
var1 = 'abcdef' 
print(var1[1:3]) #取子字符串
print(var1[2])   #取单个字符
print(var1)      # 输出完整字符串
print(var1[2:])       # 输出从第三个字符开始的字符串
print(var1*2)       # 输出字符串两次
print(var1+'haa')  # 输出连接的字符串
print(var1[1:4:2])  #第三个参数用来接收截取的步长（头尾之间每隔多少位截取一次）

#字符串输出拼接操作
var2 = 'new'
var3 = 'haha'
# % 方式拼接
# 字符串:%s 整数:%d 浮点:%f
print('1 使用 % 方式拼接')
print('hah this is my %s print'%var2) #使用%穿插
print('%s this is my %s print'%(var3,var2)) #使用%穿插2个以上
print('this is my %s number %d'%(var3,2)) #字符串+数字
# format 方式拼接
print('2 format 方式拼接')
print('{} this is my {} print'.format(var3,var2)) #简洁版
print('{1} this is my {0} print'.format(var2,var3)) #对号入座版
print('{1:.2f} this is a {0:.2f}'.format(3.1322,212)) #控制打印位置+精度
    #{位置,精度}  也可以不加位置 {:.2f} 
    #填充 规范输出格式 < 补右边 >补左边 
print('{:1<4d}'.format(2)) # < 填充右边 共4位补1
print('{:0>5d}'.format(2)) # > 填充左边 共5位 不足补0
print('{:>4d}'.format(2)) # < 填充左边 不写默认补空格
print('{:>10}'.format(var1)) # 填充左边 
#其他
print('hah',var2,var3)
print('haha'+var2+var3)

    
    
    
    
    
    
    
    