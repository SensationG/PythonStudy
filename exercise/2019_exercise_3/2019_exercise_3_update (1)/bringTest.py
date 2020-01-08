import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

base_url='https://tw.news.yahoo.com/basketball'
#items='Brexit'
#search_params={'q':items}
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}
r=requests.get(base_url,headers=my_headers)#params=search_params,
r.encoding='utf-8' #网页乱码
soup=BeautifulSoup(r.text,'html.parser')

t_list=soup.select('#mrt-node-YDC-Stream li')
include_words = ['nba', 'NBA', '勇士', '湖人']#只查找包含这几个关键字的
print(len(t_list))
numOpen = min(20, len(t_list))

a=0
for i in range(numOpen):
    content=t_list[i].find('h3').find('a')
    title=content.text
    link=content['href']
    link = unquote(link)
    if any(w in link for w in include_words): #限制关键字 
        link='https://tw.news.yahoo.com/basketball'+link
        print(title)
        print(link)
        print()
        a=a+1
print(a)
      
                   

    
