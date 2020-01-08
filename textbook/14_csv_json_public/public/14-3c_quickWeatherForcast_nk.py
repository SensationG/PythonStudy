#! python3
# quickWeather.py - Prints the current weather for a location from the command line.
#--------------------使用API获取*多地区*（预测）天气信息 处理json档案2----------------------------

import json
import requests
import pprint

location = 'Taipei,TW'

# Download the JSON data from OpenWeatherMap.org's API
APIKey='800585ee497425b9a06893c710571eb0'
url = 'http://api.openweathermap.org/data/2.5/forecast?units=metric&q=%s&appid=%s' % (location, APIKey)

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.

# 方式1
#weatherData = json.loads(response.text)
# 方式2
weatherData = response.json() #读取json档 
#pprint.pprint(weatherData)
#print(weatherData)

# Print weather descriptions.
wd = weatherData['list'] #选出天气预测的list
print(wd[0]) #选出其中一个来分析打印格式
print('5 Day weather forecast in %s:' % (location))
#print(wd[0])
for w in wd:
    #print(w['dt_txt'],'-', str(w['main']['temp']) + ', ', w['weather'][0]['description'])
    print('{:s} - {:.2f}\u2103 {:s}'.format(w['dt_txt'], w['main']['temp'], w['weather'][0]['description']))
print()

