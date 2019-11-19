"""
Converting list into dictionary with index as key

"""
#把list表转到dict中

list = [2, 55, 27, 15, 39]

dict1={}

for k, v in enumerate(list):
    print("k, v:", k, v)
    dict1[k] = v

print('dict1: ',dict1)    

#dict1 = {i:v for i,v in enumerate(list)} #方法2
#print(dict1)
#del (dict) #出现dict not callable时使用
dict2 = dict(enumerate(list)) #方法3
print('dict2:',dict2)

# 產生排序後的 key list
# 按dict2的value进行排序，仅返回排序后的key
sorted_index = sorted(dict2, key=dict2.get, reverse=True)
print(sorted_index) 

for i, v in enumerate(sorted_index[:2]):
    print("Top#%d: %2d" % (i+1, dict2[v]))
    
sorted_items = sorted(dict2.items(), key=lambda x: x[1], reverse=True)
print(sorted_items) 

for i, v in enumerate(sorted_items[:2]): #输出index + value
    print("Top#%d: %2d" % (i+1, v[1])) # v[0] 是字典中key v[1]是value
for i, v in sorted_items[:2]: #输出key+value
    print("Top#%d: %2d" % (i, v)) 