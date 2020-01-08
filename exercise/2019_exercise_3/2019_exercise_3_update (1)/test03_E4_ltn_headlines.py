# -*- Coding: utf-8 -*-

import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlsplit
import random

url = 'http://www.ltn.com.tw'

UserAgentList = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"]
    
my_user_agent = UserAgentList[random.randint(0, len(UserAgentList)-1)]
my_headers = {'User-Agent': my_user_agent}

r = requests.get(url, headers=my_headers)

#print(r.raise_for_status())
#print(r.status_code)

# Get crawling results 
soup = BeautifulSoup(r.text, 'html.parser')

page_title = soup.select('head  title')[0].text
print('Crawling %s ...\n' % (page_title))

# Retrieve top five search result links.
linkElems = soup.select('div.swiper-slide a') # <a> tag under ".r" class
#print(len(linkElems))
numOpen = min(10, len(linkElems))

skip_words = ['TAIPEI TIMES']
bad_urls= ['https://cache.ltn.com.tw/']

for i in range(numOpen):
    title = linkElems[i].text.strip('\n')
    link = linkElems[i].get('href') # get url from <href> tag
    link = unquote(link)
    #print(title)
    #print("原始 link: " + link)

    #print(urlsplit(link))
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(link))
    
    # 去除標題包含特定停用字, 以及基本網址在排除名單的連結
    # print(any(w in title for w in skip_words))
    if not any(w in title for w in skip_words) and base_url not in bad_urls:
        print(title)
        print(link)
        #print(base_url)
        print()
        #webbrowser.open(link)
        
input("Press any key to continue...")