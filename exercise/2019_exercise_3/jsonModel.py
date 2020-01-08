# 处理返回档案是json档的模板

import json
import requests
import pprint
import datetime

# 1 url
url=''
# 2 返回json档案（str类型）
r = requests.get(url)
r.raise_for_status()
# 3 解析json档案-->转为dict
weatherData = json.loads(r.text) #json.loads(type=str)
# 或 weatherData =  response.json()

# 4 美化打印 方便分析内容
pprint.pprint(weatherData) #不打乱原格式打印

# 5 获取信息 示例
bikes = r.json()['retVal'] #json转为字典并取字典中的retVal
desc = weatherData['weather'][0]['description'] #weather中是一个大list
temp = weatherData['main']['temp']
# 时间处理
date = datetime.datetime.fromtimestamp(weatherData['dt'])#时间格式化
print(date)
#date_str = date.strftime('%Y-%m-%d %H:%M:%S')
date_str = date.strftime('%Y-%m-%d %I:%M %p') # 00:00 AM/PM