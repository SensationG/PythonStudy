#! python3
# quickWeather.py - Prints the current weather for a location from the command line.
#--------------------使用API获取单地区天气信息 处理json档案----------------------------

import json
import requests
import pprint
import datetime

location = 'Taipei,TW'

# API地址
APIKey='800585ee497425b9a06893c710571eb0' #放入你自己的APIKey
url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q=%s&appid=%s' % (location, APIKey)

response = requests.get(url)
#请求不成功时 调用Response.raise_for_status() 来抛出异常
response.raise_for_status()

# response.text：获取返回的信息 ，是json档案 解析json档案为字典
weatherData = json.loads(response.text) 
#weatherData =  response.json()
pprint.pprint(weatherData) #不打乱原格式打印
print(type(weatherData)) #dict类型

# 获取weatherData中的信息
desc = weatherData['weather'][0]['description'] #weather中是一个大list
temp = weatherData['main']['temp']
date = datetime.datetime.fromtimestamp(weatherData['dt'])#时间格式化
#date_str = date.strftime('%Y-%m-%d %H:%M:%S')
date_str = date.strftime('%Y-%m-%d %I:%M %p') # 00:00 AM/PM

print('Current weather in %s:' % (location))
print('{:s} - {:s}, {:.2f}\u2103'.format(date_str, desc, temp))
print()


