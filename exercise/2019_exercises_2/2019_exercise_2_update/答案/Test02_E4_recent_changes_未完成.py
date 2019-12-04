# -*- coding: utf-8 -*-
"""
Find files modified within n hours from now
"""
#------------------需要获取子资料夹里面的文件的内容 使用这种walk的方式
import os
from datetime import datetime, timedelta


# 定義 48 小時前的datetime
def timesup(mtime):
    dt = datetime.now() #呼叫电脑当前时间
    #print('current datetime:', dt)
  
    hours48 = timedelta(hours=48) #定义48小时  
    dt_48 = dt - hours48 #时间加减
    #print('48小时前的时间：',dt_48)
    #比较时间是否在48小时内
    if mtime>dt_48:
        return True
    else:
        return False

path = os.getcwd()
path1= os.path.dirname(path) #改装，获取指定文件夹下的所有文件



#folder：列出该路径下的目录 subfolder：列出所有文件夹名称 filenames：列出该路径下的所有文件名
for folder, subfolder, filenames in os.walk(path1): #os.walk('.') os.walk不但会检测当前目录 还会进文件夹检测里面的文件
    
    #print("[folder] -> ", folder)
    
    #检测文件
    for file in filenames:

        #print(file, end='\t')
        # 取得檔案的修改時間, 單位：秒
        mtime_ts = os.stat(os.path.join(folder,file)).st_mtime

        # 轉換 timestamp 到 datetime 物件
        mtime =  datetime.fromtimestamp(mtime_ts)
        #print(mtime) #每个档案的修改日期
        
        # 比較修改時間是否在最近 n hours 之內
        if timesup(mtime):
            print('48小时内修改过的文件：',file,mtime)
    
    #检测文件夹
    for fold in subfolder:
        mtime_ts = os.stat(os.path.join(folder,fold)).st_mtime
        mtime =  datetime.fromtimestamp(mtime_ts)
        if timesup(mtime):
            print('48小时内修改过的文件夹：',fold,mtime)
        else:
            print('未修改过的文件夹',fold,mtime)
    print()

