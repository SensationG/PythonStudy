# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:32:06 2019

@author: hhw
"""

'''
1. 產生不重覆的9組樂透開獎號碼， 每一組有6個不重覆的號碼, 每個號碼在 1與 100 之間 (1 <= n < 100)
 以 3 × 3 排列如下：
'''
#random
import random
#第一题
print('D1题')
lotto=[]
i=1
while i<10:
    lootos = random.sample(range(1,100),k=6)
    lootos.sort() #排序之后才能判断是否重复
    if lootos not in lotto:
        lotto.append(lootos)
        i+=1
    else:
        continue

for i in range(len(lotto)):
    if(i+1)%3==0:
        print(lotto[i]) #为3倍数的时候换行
    else:
        print(lotto[i],end='')
    
    
#第二题：题目给出的字典
grade_dict = {'s1071234':[75, 75, 75, 75], 's1071235': [70, 70, 70, 70], 
                 's1071237':[71, 72, 78, 79], 's1071239': [74, 85, 76, 75],
                 's1071246':[85, 85, 85, 75], 's1071248': [85, 85, 95, 75],
                 's1071250':[80, 80, 80, 80], 's1071253': [71, 75, 74, 75],
                 's1071258':[72, 78, 78, 72], 's1071266': [74, 74, 74, 74]}
#2.1
print('2.1题')
for grade in grade_dict:
    list=grade_dict[grade]
    sum=0
    for i in list:
        sum+=i
    sum/=4
    print('#{}:grade average = {:.2f}'.format(grade,sum))
 
#2.2
print('2.2题')
AvgGrade = {}
for grade in grade_dict:
    list=grade_dict[grade]
    sum=0
    for i in list:
        sum+=i
    sum/=4
    AvgGrade[grade]=sum #把成绩平均值存入字典
    
#字典内部按value进行排序 从大到小所以reverse=True 输出是list
AvgGrade_1=sorted(AvgGrade.items(),key=lambda x:x[1],reverse=True)
#遍历list AvgGrade_1
for key,value in AvgGrade_1[:3]:
   print('#{}:grade average = {:.2f}'.format(key,value))


'''
字典内部按key排序 输出为list
test_data_0=sorted(AvgGrade.keys())
'''







