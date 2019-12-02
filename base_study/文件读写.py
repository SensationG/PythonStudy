# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:18:09 2019

@author: hhw
"""

#
# 1 文件读取： 一次读取一行
a=''
with open("s4_read.txt", "r", encoding='utf-8') as f:
  for line in f:
      #print(line.strip())
      a+=line.strip() #记录在字符串中
      a+='/n'
# 2 文件写入: 文件存在则会覆盖里面的内容，若文件不存在会自动创建并写入
r = open("s4_demofile1.txt", "w", encoding='utf-8')
r.write(a) #边遍历边写入在test02 mergefile中
r.close #写完后需要close 才能完成写入

# 3 检测文件是否存在/移除文件
'''
import os
if os.path.exists("s4_demofile1.txt"): #检查文件是否存在
  os.remove("s4_demofile1.txt")   #移除文件
  print("s4_demofile1.txt removed")
else:
  print("The file does not exist.")
'''
# 4 累计文件中的字数
line_cnt = word_cnt = char_cnt = 0

with open("s4_demofile1.txt", 'r',encoding='UTF-8') as f:
    for line in f: #一次读一行
        line_cnt += 1 #累计行数
        words = line.strip('\n').split(' ') #分离出每个单词
        word_cnt += len(words) #累加words(list)的长度（长度即单词个数）
        #累计所有单词的所有字母的数量
        char_cnt += sum([len(x) for x in words]) #把每个单词取出来，用len统计每个单词的长度，并用sum累加
        
print('%d line(s)' % (line_cnt))
print('%d word(s)' % (word_cnt))
print('%d character(s)' % (char_cnt))
print()

# 5 统计文件中每个单词的重复次数/输出重复前五
words_dict={}
with open("s4_demofile1.txt", 'r',encoding='UTF-8') as f:
    for line in f: 
        words = line.strip('\n').split(' ')
        for x in words:
            if x not in words_dict:
                words_dict[x]=1
            else:
                words_dict[x]+=1

words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
print(words_dict[0:5])

# 6 heapq模块 Count模块 快速排序并取出字典中的值


