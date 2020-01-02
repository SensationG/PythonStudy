#e8-3-1抓取台銀匯率資訊
import requests
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime, strptime, mktime
from os.path import exists
import os

res = requests.get("http://rate.bot.com.tw/xrt?Lang=zh-TW")
html = res.text
bsObj = BeautifulSoup(html, "lxml")
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]
    currency_name = currency_name.replace("\r","")
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[2].contents[0]
    print(currency_name, currency_rate)
    file_name = "e8-3-1" + currency_name + ".csv"
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if not exists(os.path.join("money",file_name)):
        data = [['時間', '匯率'], [now_time, currency_rate]]
    else:
        data = [[now_time, currency_rate]]
    if not os.path.exists("money"): #建立输出文件夹
        os.mkdir("money")
    with open(os.path.join("money",file_name), "a", newline='')as f:
        w = csv.writer(f)
        w.writerows(data)
      
    
