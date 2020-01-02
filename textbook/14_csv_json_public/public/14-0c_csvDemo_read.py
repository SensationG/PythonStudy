import csv
#-------------------------------读取CSV档案----------------------------
# Read csv directly 每个栏位用数组保存
with open('example.csv') as f:
    
    csv_reader = csv.reader(f, delimiter=',')  #读取时的分隔符号
    #headers = next(csv_reader, None) # 跳过第一行（当有栏位名称时）
    for row in csv_reader:  #按行打印
        print(type(row))
        print(row)
        print(row[0])
f.close()
   
print()     
# Read as text file 每一行用字符串保存
with open('example.csv', encoding='utf-8') as f:
    lines = f.readlines()  #效果是一次读取所有数据
    
#print(lines)
for line in lines:
    print(type(line))
    print(line)
    print(line[0])
f.close()