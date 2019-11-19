# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:39:44 2019

@author: hhw
"""
import random
grade_dict={} #成绩表
Sid = [] #student id
Tid = [] #查重用
avg1 = {} #存平均数
i=0
while i<20:
    r_int = random.randint(1071201,1071299)
    if(r_int not in Tid):
        Tid.append(r_int)
        i=i+1
        
for i in Tid:    
    a='s'+str(i)
    Sid.append(a)

for i in range(len(Sid)):
    samples = random.choices(range(66,100), k=6)
    grade_dict[Sid[i]]=samples
print('Student Scores and Average: ')
for key,value in grade_dict.items():
    avg=0
    sum=0
    for a in value:
        sum+=a
    avg=sum/6
    avg1[key]=avg
    print('#{}:{},{:.2f}'.format(key,value,avg))
    
avg2 = sorted(avg1.items(), key=lambda x: x[1], reverse=True)  
print()
print('Top 3 performed students ')
for key,value in avg2[:3]:
    print('#{}:{:.2f}'.format(key,value))
    
    
    
    
    
    
    
    