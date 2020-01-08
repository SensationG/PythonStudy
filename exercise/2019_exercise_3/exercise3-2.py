# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:30:54 2019

@author: hhw
"""
#--------------重写的台湾银行爬虫--------------
import requests
from bs4 import BeautifulSoup
from time import localtime, strftime, strptime, mktime
import os
import csv
from os.path import exists

re = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
soup = BeautifulSoup(re.text,"html.parser") 

allCountry=soup.find("tbody").find_all("tr")

for country in allCountry:
    area=country.select("div.hidden-phone.print_show")[0].text.strip() #爬取地区
    cash=country.find_all("td")[2].text #爬取汇率
    print(area,cash)
    #存储汇率到档案
    file_name = "exercise3-2" + area + ".csv"
    #存储时间记录
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    #资料输出文件夹
    if not os.path.exists(os.path.join("money",file_name)):
        data = [['時間', '匯率'], [now_time, cash]]
    else:
        data = [[now_time, cash]]
    if not os.path.exists("money"): #建立输出文件夹
        os.mkdir("money")
    with open(os.path.join("money",file_name), "a", newline='')as f:
        w = csv.writer(f)
        w.writerows(data)