# -*- coding: utf-8 -*-
""" grouping a list of numbers by range """

a = [x for x in range(10)]

# Create a group dict for saving the result
g_dict = {}

# Specify the range
r = 5 

for e in a:
    q = e//r # quotient 商數
    g = q * r # range lowerbound 組距下限
    g_dict.setdefault(g, [])
    g_dict[g].append(e)
   
print(list(g_dict.items()))
