# coding: utf-8 

#--------------------使用request请求网站（是否正确请求）/获取网站相关信息--------------------
import requests
from pprint import pprint

response = requests.get("https://en.wikipedia.org/robots.txt")

# vars(x) returns this dictionary of x' instance variables
# dir(x) returns a dictionary of x's attributes, its class's and base classes attributes
#print(dir(response)) #requsest返回网站数据后可查询的属性
#print(vars(response).keys()) #requsest返回网站数据后可查询的属性

# 返回的网站信息提取text
txt = response.text
print(txt)

# 返回的数据编码类型
print(response.encoding)

# 如果发送了一个错误请求(一个 4XX 客户端错误) Response.raise_for_status() 抛出异常：
# 如果为None 那么请求正确
print(response.raise_for_status())

#  http状态码 正确访问：200
print(response.status_code)

# response headers 返回请求头
#print(response.headers)
#print(json.dumps(dict(response.headers), indent=4))
pprint(dict(response.headers)) # transform to a dict first 
print()

# get response headers content 请求头类型
print(response.headers['content-type'])
