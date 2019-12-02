# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:24:16 2019

@author: hhw
"""

import os

# 1 返回当前工作目录
print (__file__) #返回当前全路径
curDir = os.getcwd()
print(curDir)
# 2 返回当前目录下的所有文件和文件夹
dirs=os.listdir(curDir)
for file in dirs:
    print(file)
# 3 新建/删除文件夹（在当前工作目录下)
os.rmdir('newDir')  #删除文件夹
os.mkdir('newDir')  #创建文件夹
# 4 更改文件名称
#os.rename('3.txt','3.txt')

# 5 join 组合路径
pathname = os.path.join(curDir, 'test', 'test1.py')
print('pathname-->',pathname)
# 6 获取当前的路径名/文件名
print ("dirname", "=>", os.path.dirname(pathname))
print ("basename", "=>", os.path.basename(pathname))
# 7 返回档案大小
print(os.path.getsize(__file__))

# 8 检测文件/目录是否存在
i=os.path.isdir('C:\\Windows\\System32') #目录
i=os.path.isfile('C:\\Windows\\System32\\calc.exe') #文件

# 9 使用stat获取文件的相关信息（创建时间等）
import time
import datetime
st = os.stat("s4_demofile1.txt")
print(time.strftime("%Y-%m-%d %H:%M:%S %z", time.localtime(st.st_mtime))) #%z为时区

# 10 设置时区，转换为该时区的时间打印
from dateutil.tz import gettz
tpe_tz = gettz("Asia/Tokyo")
mtime = datetime.datetime.fromtimestamp(st.st_mtime, tpe_tz) #上面的st
print(mtime.strftime("%Y-%m-%d %H:%M:%S %z"))