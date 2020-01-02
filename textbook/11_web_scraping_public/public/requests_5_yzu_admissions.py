# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

#------------------------------------爬yzu官网招生公告，包含特定关键字爬取 div存在空格的select--------------------------------------
#-------------------------url处理---------------------------
base_url = 'https://www.yzu.edu.tw/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}

r = requests.get(base_url, headers=headers)

#print(r.raise_for_status())
#print(r.status_code)
#print(r.url)
# Get crawling results 
#--------------------------内容处理--------------------------
soup = BeautifulSoup(r.content, 'html.parser')

page_title = soup.select('head  title')[0].text #爬网页的标题栏
print('Crawling %s 招生訊息...\n' % (page_title))
 
# Retrieve top five search result links. div存在空格的写法  
linkElems = soup.select('div.slideCon.mod_admissions div.linkItem a') #爬招生公告列表
print(len(linkElems))
numOpen = min(10, len(linkElems))

include_words = ['碩士班', '博士班', '大學部']#只查找包含这几个关键字的

for i in range(numOpen):
    title = linkElems[i].getText() #.text
    link = linkElems[i].get('href') # get url from <href> tag
    link = unquote(link)#把 % 開頭的16進位網址轉換為正常文字
    
    # print(any(w in title for w in include_words))
    # title 一定要有 ['碩士班', '博士班', '大學部'] 其中一個
    
    if any(w in title for w in include_words): #any：在关键字中有任意一个字存在 true 先执行后半句，再执行前半句
         link = 'https://www.yzu.com.tw' + link
         print(title)
         print(link)
         print()
    else:
         continue 
