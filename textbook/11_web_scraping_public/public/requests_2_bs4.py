# -*- coding: utf-8 -*-

#---------------------soup配合find,select使用--------------------------------
import requests
from bs4 import BeautifulSoup

r = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
page = r.content
#使用soup解析网页
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify()) #美化代码后打印 （打印出来不会太乱较好阅读）

# Search for any p tag that has the class outer-text
print("--> Find all p tags ...")
#搜寻所有p标签，且class包含outer-text
print(soup.find_all('p', class_='outer-text'))

print("--> Find all p tags ...")
#同上
print(soup.find_all('p', 'outer-text'))
print()

# Find the first p tag that has the class outer-text
# 搜寻第一个p标签
print("--> Find the first p tag ...")
#attrs中为指定的class/id等 可以限制多个条件
print(soup.find('p', attrs={'class': 'outer-text'}))
print()
print("--> Find specific p tag ...")
#搜寻第一个p标签，id=first 只能限制一个条件
print(soup.find('p', id='first'))
print()

# 使用select搜寻class
print("--> Find all p tags under div ...")
print(soup.select("div p")) 

print(soup.select("div > p"))#有大于号的不会捞到孙子的p，只会捞下一层 
