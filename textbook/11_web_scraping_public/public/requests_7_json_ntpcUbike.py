# coding: utf-8

# YouBike in New Taipei City
# https://data.ntpc.gov.tw/od/detail?oid=71CD1490-A2DF-4198-BEF1-318479775E8A

#-------------------------------爬取政府开放资料平台-台北ubike信息-json处理-----------------------

import requests
import pprint

# 纯手动时间格式处理的function
def mday_2_date_str(mday_str):
    #"mday":"20180530214819"
    yr = mday_str[0:4] #选取前几位
    mo = mday_str[4:6]
    dt = mday_str[6:8]
    hr = mday_str[8:10]
    mi = mday_str[10:12]
    se = mday_str[12:]
    date = yr + '-' + mo + '-' + dt
    time = hr + ':' + mi + ':' + se
    return date + ' ' + time

# 網址    
base_url = 'http://data.ntpc.gov.tw/api/v1/rest/datastore/'
data_id = '382000000A-000352-001'
url = base_url + data_id

r = requests.get(url) #返回json信息

print(r) #状态码 

pprint.pprint(r.json()) #将json档转为dict 并有格式地打印
sites = r.json()['result']['records'] #取出字典result中的records 返回list类型
#print(type(sites))# return list

sel_sites= [] #存储资料 后面选择板桥区资料作为选取目标
#sel_sites = [s for s in sites if s["sarea"] == "板橋區"] 快速写法
for s in sites:
    if s["sarea"] == "板橋區":
        sel_sites.append(s)

# 打印出板桥区ubike的各种信息
for i, s in enumerate(sel_sites): 
    print('%2d. %s: %s (%s, %s) %2d %s' % \
            (i+1, s['sna'], s['ar'], str(s['lat']), str(s['lng']), \
            int(s['sbi']), mday_2_date_str(s['mday']))) #mday_2_date_str 时间格式处理函数

# "sna":"大鵬華城","tot":"38","sbi":"3","sarea":"新店區","mday":"20180530214819",
# "lat":"24.99116","lng":"121.53398","ar":"新北市新店區中正路700巷3號",
