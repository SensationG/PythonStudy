# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:29:24 2018
Count lines, words, characters in text file: s4_read.txt

"""
# 输入文件名打开文件 累计文件字数
in_filename = input('Enter file name: ')

line_cnt = word_cnt = char_cnt = 0

with open(in_filename , 'r',encoding='UTF-8') as f:
    for line in f: #一次读一行
        print(line)
        line_cnt += 1
        words = line.strip('\n').split(' ') ##分离出每个单词
        print(words)
        word_cnt += len(words)  #累加单词的个数（计算一共有几个单词）
        #累计单个字（英语单字）数量
        char_cnt += sum([len(x) for x in words]) #把每个单词才出来，用len统计每个单词的长度，并用sum累加
        
print('%d line(s)' % (line_cnt))
print('%d word(s)' % (word_cnt))
print('%d character(s)' % (char_cnt))
