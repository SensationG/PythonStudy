#! python3
# quickWeather.py - Prints the current weather for a location.

#--------------------使用API获取*多地区*天气信息 处理json档案----------------------------
# 与2仅是打印方式不同
import json, requests,  pprint
from datetime import datetime

location = 'Taipei,TW'

# Download the JSON data from OpenWeatherMap.org's API
APIKey='800585ee497425b9a06893c710571eb0'
url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q=%s&appid=%s' % (location, APIKey)

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text) #json转字典
#weatherData =  response.json()
pprint.pprint(weatherData)#美化格式打印


# Print weather descriptions.
desc = weatherData['weather'][0]['description']
temp = weatherData['main']['temp']
date = datetime.fromtimestamp(weatherData['dt'])
#date_str = date.strftime('%Y-%m-%d %H:%M:%S')
date_str = date.strftime('%Y-%m-%d %I:%M %p') # 00:00 AM/PM

print('Current weather in %s:' % (location))
print('{:s} - {:s}, {:.2f}\u2103'.format(date_str, desc, temp))
print()

