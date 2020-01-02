# coding: utf-8

import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import requests
#------------需要先安装驱动 模拟浏览器操作-----
# specify the url
url = 'https://www.bloomberg.com/quote/SPX:IND'

gecodriver_path = 'D:/python资料库/exercise/2019_exercise_3/chromedriver'

my_headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}

# query the website and use.read() command to read the data
resp = requests.get(url, headers=my_headers)
print(resp.status_code)
page = resp.text

# make a soup
soup = BeautifulSoup(page, 'html.parser')

# check the tile
title = soup.select('head > title')[0].text
print("title first try:", title)

if "robot" in title: # use selenium instead
    browser = webdriver.Firefox(executable_path=gecodriver_path)
    browser.get(url)
    page = browser.page_source
    # browser.quit()
    soup = BeautifulSoup(page, 'html.parser')
    # title of the page
    print("title second try:", soup.title.text)

# Take out the <div> of name and get its value
names = soup.select('h1[class*="companyName"]')
name = names[0].text.strip() # strip() removes starting and trailing whitespaces
print (name)

# get the index price
#price_box = soup.find('div', attrs={'class':'price'})
prices = soup.select('span[class*="priceText"]')
price = float(prices[0].text.replace(',',''))
print (price)

# Get market status
markets = soup.select('div[class*="marketStatus"] span')
market_status = markets[0].text
print(market_status)

# get the date, 
# Market Open As of 09:30 AM EST 11/20/2018 EDT, 
# Market Closed As of 11/20/2018 EDT
dates = soup.select('div[class*="time_"]')
date = dates[0].text.split()[2]
print(date)

# open a csv file with append, so old data will not be erased
with open('SP500_Index.csv', 'a',  newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, date, market_status])