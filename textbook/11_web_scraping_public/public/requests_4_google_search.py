# -*- coding: utf-8 -*-
# lucky.py - Opens several Google search results.
#----------------------------抓Google搜寻结果--------------------------
import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

print('Googling...\n') # display text while downloading the Google page

#-------------------------url处理---------------------------
# Google search parameters：http://www.google.com/search?hl=en&lr=lang_en&q=example
google_url = 'https://google.com/search?'
query_terms = 'Brexit'  # '農禪寺', 'Brexit' 'grasshopper 3d' #搜索内容
host_lang = 'en' # zh-TW, vi, en
search_lang = 'lang_en'  # lang_zh-TW, lang_vi

search_params = {'q': query_terms, 'hl': host_lang, 'lr': search_lang}

# 設定爬蟲的 headers
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}

#res = requests.get(google_url + 'q=' + query_terms)
res = requests.get(google_url, params=search_params, headers=my_headers)
print(res.url)
#res.raise_for_status()

#-------------------------内容处理---------------------------
soup = BeautifulSoup(res.content, 'html.parser') #一般要下载图片，文件才要content
#rint(res.text)

# Retrieve top five search result links.
linkElems = soup.select('.r') # ".r" class 搜寻到全部class="r"的div
numOpen = min(10, len(linkElems)) #选取前十个结果

for i in range(numOpen):
    title = linkElems[i].a.text  # get first <a> tag 另一种获取a标签的方式
    link = linkElems[i].a.get('href') # get url from <href> tag
    link = unquote(link) #把 % 開頭的16進位網址轉換為正常文字
    print(link)
    if link.startswith('/url'):
        # /url?q=http://www.grasshopper3d.com/&sa=U&ved=0ahUKEwjS5oKg2s7WAh...
        #link.find("q"): index of q
        #link.find("&"): index of first &
        siteurl = link[link.find("q")+2:link.find("&sa")]
    elif link.startswith('/search?q'): # /search?q=grasshopper+3d&dcr=0&ie=UTF-8&prmd=ivns...
        siteurl = 'https://google.com' + link
    else:
        siteurl = link
    
    # Open a browser tab for each result.
    #webbrowser.open(siteurl) 在浏览器中打开网址
    #print("處理過link: " + unquote(siteurl))
    print(title)
    print()