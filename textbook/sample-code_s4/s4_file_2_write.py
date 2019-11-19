# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:59:04 2018

Write to an Existing File

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

"""
# ------------写文件----------------

# Open the file and append content to the file:
# mode=a ：新的内容将会被写入到已有内容之后。
#          如果该文件不存在，创建新文件进行写入。
print('--------追加文件内容-----------')
f = open("s4_demofile2.txt", "a")
f.write("\rNow the file has one more line!\n")
# \r 表示换行 光标在上一行？

# Loop through the file line by line:
#'--------打开文件 查看被追加的内容-----------'
f = open("s4_demofile2.txt", "r", encoding='utf-8')
for x in f:
    print(x.strip('\n'))

# Open the file "s4_demofile2.txt" and overwrite the content:
# mode=w 如果文件存在，原有的内容会被删除。若不存在则新建
print('--------文件写入 w-----------')
f = open("s4_demofile2.txt", "w", encoding='utf-8')
f.write("Woops! the content overwritten! 中文字")

#Loop through the file line by line:
#查看写入的内容
f = open("s4_demofile2.txt", "r", encoding='utf-8')
for x in f:
    print(x)
  
