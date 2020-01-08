# coding: utf-8

# UBikes in TaoYuan City

import requests
from prettytable import PrettyTable

base_url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?'
tycParams = {'id':'5ca2bfc7-9ace-4719-88ae-4034b9a5a55c',
            'rid':'a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'}

url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'
area = "中壢區"

# Configure PrettyTable
pt = PrettyTable()
pt.field_names= ['場站', '地址', '可借車數', '緯度', '經度']
pt.align["場站"] = "l"
pt.align["地址"] = "l"
pt.align["可借車數"] = "r"

r = requests.get(base_url, params=tycParams)
#print(r.json())

# Get sites of selected area
sites_dict = r.json()['retVal']
#print(sites_dict.keys())

#for s in sites_dict.items(): #判断所在区
  #print(s[1]['sarea'])
sel_sites = [site for site in sites_dict.values() if site["sarea"] == area]

data_rows = []

for s in sel_sites:
   #新建list
    row = [s['sna'], s['ar'], int(s['sbi']), float(s['lat']), float(s['lng'])]
    data_rows.append(row) #形成二维list

# 给新建的list进行排序 自带一层遍历
data_sorted = sorted(data_rows, key = lambda x: x[2], reverse=True)

print('--- ' + area + 'uBikes - 依可借車數排序 ---')
for i, r in enumerate(data_sorted):
    #print(i+1, r)
    pt.add_row(r) # r：list 类型

print(pt)

# input("\nPress any key to continue ...")

"""
 "retVal" : {
    "2001" : {
      "sna" : "中央大學圖書館",
      "tot" : "60",
      "sbi" : "16",
      "lat" : "24.968128",
      "lng" : "121.194666",
      "bemp" : "42",
      "act" : "1",
      "sno" : "2001",
      "sarea" : "中壢區",
      "mday" : "20181110001041",
      "ar" : "中大路300號(中央大學校內圖書館前)",
      "sareaen" : "Zhongli Dist.",
      "snaen" : "National Central University Library",
      "aren" : "No.300, Zhongda Rd."
    },
    "2002" : {
      "sna" : "中壢高中",
      "tot" : "52",
      "sbi" : "17",
      "lat" : "24.960815",
      "lng" : "121.212038",
      "bemp" : "34",
      "act" : "1",
      "sno" : "2002",
      "sarea" : "中壢區",
      "mday" : "20181110001025",
      "ar" : "中央西路二段215號對面人行道",
      "sareaen" : "Zhongli Dist.",
      "snaen" : "Jhungli Senior High School",
      "aren" : "No.215, Sec. 2, Zhongyang W. Rd. (opposite)"
    },
"""