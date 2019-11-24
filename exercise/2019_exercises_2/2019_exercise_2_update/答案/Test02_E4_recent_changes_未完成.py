# -*- coding: utf-8 -*-
"""
Find files modified within n hours from now
"""

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

#folder：列出该路径下的目录 subfolder：列出所有文件夹名称 filenames：列出该路径下的所有文件名
for folder, subfolder, filenames in os.walk('.'):
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

