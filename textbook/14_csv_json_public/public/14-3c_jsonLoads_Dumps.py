

#-----------------JSON与字典互相转换---------------------
import json

# 模拟json数据
string_of_json_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

# json.loads(string): 将已编码的 JSON 字符串解码为 Python 对象（字典类型）
jsonObj = json.loads(string_of_json_data) 

print("jsonObj is a", type(jsonObj))#转换后的类型是dict
print(jsonObj)
print(jsonObj['name'])

#{'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

# 模拟字典数据
jsonObj = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}

# json.dumps(jsonObj): 将 Python 对象（字典类型）编码成 JSON 字符串
string_of_json_data = json.dumps(jsonObj)

print("strig_of_json_data is a", type(string_of_json_data))
print(string_of_json_data)
#print(string_of_json_data['name']
#'{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'