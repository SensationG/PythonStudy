# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:38:46 2019

@author: hhw

https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f
"""
import requests
# 網址    
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'

r = requests.get(url,verify=False)

bikes = r.json()['retVal'] #json转为字典并取字典中的retVal

sort_bikes = sorted(bikes.items(),key=lambda d:int(d[1]['sbi']),reverse=True)

for i,s in enumerate(sort_bikes):
    print(i+1,'[場站名稱：',s[1]['sna'],'地址:',s[1]['ar'],'目前車輛數:',s[1]['sbi'],'经度：',s[1]['lat'],'维度：',s[1]['lng'],']')
