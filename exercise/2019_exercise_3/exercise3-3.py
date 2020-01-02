# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:32:05 2019

@author: hhw
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
city_data = requests.get("http://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0")

soup = BeautifulSoup(city_data.text,"html.parser")
citys=soup.find("select").find_all("option")
city1=[] #存放爬取的所有城市
for i in citys:
    city1.append(i.text)
print(city1)

#该网站只能用post方式传入信息查询
for index,city in enumerate(city1):
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}    
    res = requests.post('http://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    if index==0:
        df_7_11_store = pd.read_html(res.text, header=0)[0]
        df_7_11_store['縣市'] = city
    if index>0:
        df_7_11_store_ = pd.read_html(res.text, header=0)[0]
        df_7_11_store_['縣市'] = city
        #dataframe的append方法 标准做法
        df_7_11_store = df_7_11_store.append(df_7_11_store_)
   #打印出進度
    print('%2d) %-*s %4d' % (index+1, 5, city, pd.read_html(res.text, header=0)[0].shape[0]))

df_7_11_store.to_excel('7_11門市3.xlsx', encoding="UTF-8", index=False) 

