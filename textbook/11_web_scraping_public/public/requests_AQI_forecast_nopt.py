# coding='utf-8'

import csv
import random
import requests
#from prettytable import PrettyTable
# http://zetcode.com/python/prettytable/

#----------------------------读取返回的CSV档处理--不使用图表输出-------------------------------

# Read csv
url = 'https://opendata.epa.gov.tw/ws/Data/AQFN/?$format=csv' #完整的路径
url = 'https://opendata.epa.gov.tw/api/v1/AQFN?$skip=0&$top=1000&$format=csv' #设定开始行和结束行

UserAgentList = [ #表头
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"]
    
my_user_agent = UserAgentList[random.randint(0, len(UserAgentList)-1)] #随机选一个浏览器 header
print('浏览器头:',my_user_agent) 
my_headers = {'User-Agent': my_user_agent} #设置浏览器头

# pt = PrettyTable()
# pt.field_names= ['Area', 'MajorPollutant', 'AQI', 'ForecastDate', 'PublishTime']
# pt.align["Area"] = "l"
# #pt.align["MajorPollutant"] = "l"
# pt.align["AQI"] = "r"

response = requests.get(url, headers=my_headers, verify=False) #处理csv时，使用verify不验证

#---------------------------内容处理--------------------------------
# read from response.text (a string)
# 判断返回值是否成功响应
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    # 读取csv档案
    csvReader = csv.reader(response.text.splitlines())
    
    headers =  next(csvReader, None) # read first row

    AQI_data = [] # 存储csv中的数据
    
    # 一行一行讀取 csv reader 物件的內容，並加入 AQI_data 陣列
    for idx, row in enumerate(csvReader):
        # 给列表新增一个标号列且输出从内容的第二列开始
        row = [idx] + row[1:] 
        AQI_data.append(row)
        print(row)
    
    # pt图表设定标题栏内容 从指定欄位抽取
    # pt.field_names = headers[1:5] + headers[7:8]
    #print(headers)

    # Sort AQI_data by date, then by pseudo index 排序优先级
    AQI_sorted = sorted(AQI_data, key=lambda x: (x[4], -x[0]))
    
    for row in AQI_sorted:
        # print(row)
        # ['Content', 'Area', 'MajorPollutant', 'AQI', 'ForecastDate',
        #  'MinorPollutant', 'MinorPollutantAQI','PublishTime']

        rec = row[1:5] + row[7:8] # list1 + list2, 只取指定欄位的數據
        rec = [x.strip() for x in rec] #取出数据的前后空格
        
        rec = ['-- N/A --' if x == '' else x for x in rec] # 空值的欄位填入 -- N/A --
        print(rec)
        #print("{:3s}\t{:8s}\t{:>4s}\t{:12s}{:16s}".format(rec[0], rec[1], rec[2], rec[3], rec[4]))
        #pt.add_row(record)
        
    #print(pt)    
        