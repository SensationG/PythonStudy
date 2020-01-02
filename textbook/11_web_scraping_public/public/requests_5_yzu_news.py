#! python3
#----------------------------------爬取yzu新闻与信息模块，排除不要的部分stopword-----------------------
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import webbrowser

#-------------------------url处理---------------------------
base_url = 'https://www.yzu.edu.tw/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}

r = requests.get(base_url, headers=headers)

#print(r.raise_for_status())
#print(r.status_code)

#--------------------------内容处理--------------------------
# Get crawling results 
soup = BeautifulSoup(r.content, 'html.parser')

page_title = soup.select('head  title')[0].text
print('Crawling %s 新聞...\n' % (page_title))

# Retrieve top five search result links.
# Select all div.linkItem element inside div.slideCon.mod_news
# then select all <a> tags inside div.linkItem
linkElems = soup.select('div.slideCon.mod_news div.linkItem a')
#print(len(linkElems))
numOpen = min(10, len(linkElems))

stop_words = ['詳細內容', '遠東商銀']

for i in range(numOpen):
    #print(i)
    title = linkElems[i].getText()
    link = linkElems[i].get('href') # get url from <href> tag
    link = unquote(link)#把 % 開頭的16進位網址轉換為正常文字
    #print(title)
    # print(any(w in title for w in stops_words))
    # title 没有 ['詳細內容', '遠東商銀'] 其中一個
    if not any(w in title for w in stop_words):
        link = 'https://www.yzu.edu.tw' + link
        print(title)
        print(unquote(link))
        print()
        # Open a browser tab for each result.
        #webbrowser.open_new(link)
    else:
        continue 