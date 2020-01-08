#自由时报头条新闻
import requests
from bs4 import BeautifulSoup

url='https://www.ltn.com.tw/'
r=requests.get(url)
#print(r)#200
soup = BeautifulSoup(r.text,"html.parser")

# 爬取的版块
znews=soup.select('.first_part .focus .swiper-wrapper')

#限制广告 特定关键字
ad_url=['https://cache.ltn.com.tw/','https://pv.ltn.com.tw/']
ban_words=['Taipei Times','小英','黑鷹'] 

news=znews[0].find_all('a')
for new in news:
    title=new.text.strip()
    link=new['href'].strip()
    if not any(w in title for w in ban_words): #限制关键字
        if not any(i in link for i in ad_url): #限制广告
            print(title)
            print(link)
            print()  