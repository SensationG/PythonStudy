# -*- coding: utf-8 -*-
""" grouping a list of numbers by range """
#--------------字典中的---数据分组--------------------
a = [x for x in range(10)]

# Create a group dict for saving the result
g_dict = {}

# Specify the range
r = 5 

for e in a:
    q = e//r # quotient 整除
    g = q * r # range lowerbound 組距下限 
    g_dict.setdefault(g, []) #[]是append数字 ''是append str类型
    g_dict[g].append(e)
   
print(list(g_dict.items()))

h_dict={} #测试
for i in range(10):
    h_dict.setdefault('a',[])
    h_dict['a'].append(i)
    
print(h_dict)