import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#------------需要先安装驱动 模拟浏览器操作-----

# Disable web notifications 
my_options = Options()
my_options.set_preference("dom.webnotifications.enabled", False)

geckodriver_path = 'C:/Users/hhw/Desktop/qlikview教學(大學部)/1004爬虫/geckodriver'
browser = webdriver.Firefox(executable_path=geckodriver_path, options=my_options)
#browser = webdriver.Chrome(executable_path='C:/Python36-32/chromedriver')

browser.get('https://www.decathlon.tw/zh/series/#s3')
#browser.save_screenshot('screenshot.png')

# Click to close pop-up window  关闭弹窗
btnElem = browser.find_element_by_class_name('closeBtn')

if btnElem.is_displayed() and btnElem.is_enabled():
    btnElem.click()
    
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"closeBtn"))).click()
"""
#  Go to 聯絡我們
linkElem = browser.find_element_by_link_text('聯絡我們')
linkElem.click()

time.sleep(5) # seconds

browser.get('http://taipeiads.com')
browser.find_element_by_id('policy-close').click() #点击协议框
html = browser.page_source
time.sleep(3) # seconds
browser.quit()

soup = BeautifulSoup(html, "html.parser")
title = soup.select('head > title')[0]
print(title.getText())

