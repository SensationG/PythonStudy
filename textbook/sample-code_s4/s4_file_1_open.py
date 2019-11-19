# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:59:04 2018

file open
"r" - Read - Default value.
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

"""
# ------------读文件-------------
# Read content
# 第一个参数是文件名，第二个参数是开启模式
# rb：以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
print('-----read方法-------')
f = open("s4_demofile.txt", "rb") #rb模式不能使用encoding
print(f.read())

# Read Only Parts of the File
print('-----read(字符串长度)方法-------')
f = open("s4_demofile.txt", "r", encoding='utf-8')
print(f.read(10)) #d读取字符串长度为10

# Read Lines
# 只读模式 readline只读取第一行
print('-----readline方法-------')
f = open("s4_demofile.txt", "r", encoding='utf-8')
print(f.readline())

#Loop through the file line by line:
print('-----for循环读取-------')
f = open("s4_demofile.txt", "r", encoding='utf-8')
#可以使用for循环类似读取数组的方法读取io文件
for x in f:
  print(x.strip('\n'))
  # strip删除s字符串中开头、结尾处，的\n，当括号内为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
  
## 以上读取完后需手动调用close方法，但调用前需判断open方法是否成功执行  
  
# 第二种开启文件方式，自动调用close方法，无需判断
print('-----with open 方法开启文件-------')
with open("s4_test4.csv", "r", encoding='cp950') as f:
  print(f.readlines())