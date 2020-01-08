# 处理返回结果是csv的模板

import requests
import csv

# 1 路径 返回类型为csv档案
url='' 
# 2 设置表头
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# 3 发送request请求
r = requests.get(url, headers=headers, verify=False) 

#  内容处理
# 4 判断返回值是否成功响应
if r.status_code != 200:
    print('Failed to get data:', r.status_code)
else:
    # 5 读取返回的csv档
    csvReader = csv.reader(r.text.splitlines())

    # 6 获得表头（标题栏），headers接收表头/处理表头/或略过表头
    headers = next(csvReader) # 类型list
    # 7 标题栏有乱码 处理替换
    #headers = [s.replace("\ufeff","") for s in headers[0:5]]
    print(headers) #打印标题栏

    # 8 处理内容主体
    rows = [] #存储数据
    for row in csvReader:
        print(row[0:5]) #读取0-4列
        rows.append(row[0:5]) #存储数据

# 9 使用PrettyTable图表 输出
from prettytable import PrettyTable
pt = PrettyTable()
# 10 设置表格相关属性
# pt.field_names = headers[1:5] + headers[7:8] 设定标题栏内容 从指定欄位抽取
pt.field_names= ["測站名稱", "縣市", "空氣品質指標", "空氣污染指標物","狀態"]
pt.align["測站名稱"] = "l" #设置列左对齐
pt.align["空氣污染指標物"] = "l"
pt.align["空氣品質指標"] = "r" #设置列右对齐
# 11 数据清洗 跳过不符合规定的数据
rows = [r for r in rows if len(r[2]) > 0]
# 12 数据排序 以第三列为准/设置多个(x[4], -x[0])
data_rows = sorted(rows, key=lambda x: int(x[2]), reverse=True)
# 13 添加数据到图表
for i in data_rows:
    pt.add_row(i) # pt.add_row([type=list])
print(pt)