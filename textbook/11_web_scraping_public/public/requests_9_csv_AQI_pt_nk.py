# coding: utf-8
# get and parse AQI open data

"""空氣品質指標(AQI):
SiteName(測站名稱)、County(縣市)、AQI(空氣品質指標)、Pollutant(空氣污染指標物)、Status(狀態)、SO2(二氧化硫 ppb)、CO(一氧化碳 ppm)、CO_8hr(一氧化碳8小時移動平均 ppm)、O3(臭氧 ppb)、O3_8hr(臭氧8小時移動平均 ppb)、PM10(懸浮微粒 μgm3)、PM2.5(細懸浮微粒 μgm3)、NO2(二氧化氮 ppb)、NOx(氮氧化物 ppb)、NO(一氧化氮 ppb)、WindSpeed(風速 msec)、WindDirec(風向 degrees)、PublishTime(資料建置日期)、PM2.5_AVG(細懸浮微粒移動平均值 μgm3)、PM10_AVG(懸浮微粒移動平均值 μgm3)、Latitude(緯度)、Longitude(經度)

https://data.gov.tw/dataset/40448
"""
#-------------------------------爬取政府opendata-空气质量-读取返回的csv档案-------------------

import requests
import csv
from prettytable import PrettyTable

base_url = 'https://opendata.epa.gov.tw/webapi/api/rest/datastore/'
dataid = '355000000I-000259' # 空氣品質指標
format = 'csv'
userToken = 'Add_your_userToken_here'  # 放入你的 userToken
# url = base_url + dataid + "/?format=" + format + "&token=" + userToken

# 替代網址
# url = 'https://opendata.epa.gov.tw/ws/Data/AQI/?$format=csv'
url = 'https://opendata.epa.gov.tw/api/v1/AQI?$skip=0&$top=1000&$format=csv'

r = requests.get(url, verify=False)

"""
url = base_url + dataid + "/"
AQI_params = {'format': 'csv','token': userToken}
r = requests.get(url, params=AQI_params, verify=False)
"""
#print(r.url)
rows = [] #存储0-4列数据数据

if r.status_code != 200:
    print('Failed to get data:', r.status_code)
else:
    cr = csv.reader(r.text.splitlines())
    next(cr) # skip first row 跳过第一行
    for row in cr: #写入数据0-4列
        #print(row[0:5])
        rows.append(row[0:5])

#print(rows)# 二维list
pt = PrettyTable() #绘制一个图表
pt.field_names= ["測站名稱", "縣市", "空氣品質指標", "空氣污染指標物","狀態"]
pt.align["測站名稱"] = "l" #设置列左对齐
pt.align["空氣污染指標物"] = "l"
pt.align["空氣品質指標"] = "r" #设置列右对齐

rows = [r for r in rows if len(r[2]) > 0] # 跳过aqi为0的地区

# sort data rows by AQI (should be integer) 排序 按aqi从大到小
data_rows = sorted(rows, key=lambda x: int(x[2]), reverse=True)
#print(rows)

for i in data_rows:
    pt.add_row(i) # pt.add_row([type=list])
print(pt)