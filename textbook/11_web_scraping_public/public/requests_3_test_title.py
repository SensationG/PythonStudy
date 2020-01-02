# -*- coding: utf-8 -*-

"""Test if requests gets proper page title """

#-----------------使用headers模拟浏览器访问-----------------------------------

import requests
from bs4 import BeautifulSoup

url = 'https://www.yzu.edu.tw'
#url = 'https://www.bloomberg.com/quote/SPX:IND'

#User-Agent 模拟浏览器
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}

r = requests.get(url,headers=my_headers) #verify=False

print(r.raise_for_status()) # check for bad requests
print(r.status_code)

soup = BeautifulSoup(r.content, 'lxml') # lxml为网页解析器类型，也可以用htmp.parser

print(soup.select('head title')[0].text) # 'head title'