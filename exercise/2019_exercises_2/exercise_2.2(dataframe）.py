# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:36:00 2019

@author: hhw

exercise_2 第二大题
"""
import pandas as pd


#思路 读取档案-》存储对应数组-》合并成Dataframe-》拼接-》输出
title=[] #标题存储
content=[] #正文
inside=[] #临时存内容

with open("data/zh-tw-cn2.txt", "r", encoding='utf-16') as f:
    for line in f: #一次读取一行
        inside.append(line)
#print(inside[0])

inside[0]=inside[0].replace('，',' ')
#print(inside[0])
title1,title2=inside[0].split() #title
title.append(title1)
title.append(title2)
print(title)
 
content1,content2=inside[1].split() 
content.append(content1)
content.append(content2)
print(content)

print('-----------txt合成dataframe---------')
df1=pd.DataFrame(columns=title)
#横向插入
df1=df1.append([{title[0]:content[0],title[1]:content[1]}],ignore_index=True)
print(df1)

#读取csv档案
print()
df2=pd.read_csv('data/zh-tw-cn.csv')
print(df2)

#合并
total = pd.concat([df1, df2],axis=1) #横向拼接
print(total)

#输出到CSV
total.to_csv("zh-tw-cn2.csv",index=False,encoding='utf_8_sig') 