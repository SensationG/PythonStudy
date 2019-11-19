# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:59:04 2018

#Create a New File
"x" - Create - will create a file, will fail if it exists
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

"""
print('-----------创建文件------------')
# 1 Create a file called "myfile.txt":
# mode=x 写模式，新建一个文件，如果该文件已存在则会报错。
f = open("myfile.txt", "x")

# 2 Create a new file if it does not exist:
# mode=w 创建/开启文件 若不存在则会创建，存在则会重写
f = open("myfile.txt", "w", encoding='utf-8')
f.write("Write a new line including 中文字 简体字 to myfile.txt")

# Loop through the file line by line:
# 打印写入的内容
f = open("myfile.txt", "r", encoding='utf-8')
for x in f:
    print(x)

f.close() #关闭流

# 3 Check if file exist before removing it
print('-----------文件的移除------------')
import os
if os.path.exists("myfile.txt"): #检查文件是否存在
  os.remove("myfile.txt")   #移除文件
  print("myfile.txt removed")
else:
  print("The file does not exist.")
