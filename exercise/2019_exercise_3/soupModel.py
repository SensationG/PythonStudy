#soup模板 处理html爬虫

import requests
from bs4 import BeautifulSoup

url=''
# 2 设置表头
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# 3 访问
r = requests.get(url,headers=headers)
# 4 使用soup解析
soup = BeautifulSoup(r.text,"html.parser")
# 5 使用select或find 抓取内容 示例
z1=soup.select('.first_part .focus .swiper-wrapper')#抓取class
z2=soup.find_all() #抓取标签
# 6 数据清洗
#strip() #去除前后空格
# 7 限制广告 特定关键字
ad_url=['https://cache.ltn.com.tw/','https://pv.ltn.com.tw/']
ban_words=['Taipei Times','小英','黑鷹']
#if not any(w in title for w in ban_words): #限制关键字
 #   if not any(i in link for i in ad_url): #限制广告
