# -*- coding: UTF-8 -*-

# 判断程式时间 新旧 进行档案判断 获取当前时间
import os
import time
import datetime
from dateutil.tz import gettz

st = os.stat("s4_os_2_path.py") #调用stat 返回一些信息
print(st)

'''
st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
'''

tpe_tz = gettz("Asia/Taipei") #获取时间

#时间方法1
print(time.localtime(st.st_mtime)) #获取文件的保存时间并以参数形式展现
#如果为空就是返回系统时间
print()
print(time.strftime("%Y-%m-%d %H:%M:%S %z", time.localtime(st.st_mtime))) #时间格式化

#时间方法2
#print("datetime tzinfo: " , datetime.datetime.now())#返回文件时间具体到秒（数组格式）
print("datetime tzinfo: " , datetime.datetime.now().tzinfo) #？.tzinfo

#时间方法3
# datetime.fromtimestamp(timestamp, tz) # default tz=None
mtime = datetime.datetime.fromtimestamp(st.st_mtime, tpe_tz) #上面的st
print(mtime.strftime("%Y-%m-%d %H:%M:%S %z"))

