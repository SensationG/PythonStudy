# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:05:10 2019

@author: hhw
"""
#--------------------使用模拟浏览器爬取动态网页数据-----------------------
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

geckodriver_path = 'C:/Users/hhw/Desktop/qlikview教學(大學部)/1004爬虫/geckodriver'
browser = webdriver.Firefox(executable_path=geckodriver_path)
#browser = webdriver.Chrome(executable_path='C:/Python36-32/chromedriver')
#爬取土地银行
browser.get('https://mybank.landbank.com.tw/Sign/SIGN_finf_01/Index')
#browser.save_screenshot('screenshot.png')

#找到目标物件是否显示
tableElem = browser.find_element_by_class_name('tb')
if tableElem.is_displayed() and tableElem.is_enabled():
    html = browser.page_source #显示后存储

time.sleep(5) # seconds
browser.quit()

soup = BeautifulSoup(html, "html.parser")
table_trs=soup.find("table").find("tbody").find_all("tr")
for sing_tr in table_trs:
    a=sing_tr.find_all("td")[1]
    a=a.find("div")
    print(a.text)