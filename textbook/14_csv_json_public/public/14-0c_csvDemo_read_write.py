import csv

#-------------------------CSV文件的读取与（再）写入-------------------------
# Read csv
with open('example.csv', encoding='utf-8') as csvfile:

    # csv.reader(csvfileObj): read from csv file
    csvReader = csv.reader(csvfile, delimiter=',')
    
    #一次只能有一种读取方式
    # 方式1：按行读取 使用list记录
#    for idx, row in enumerate(csvReader):
#        print(type(row))#list
#        print('Row #' + str(idx) + ' ' + str(row))
    # csv.reader 物件已到盡頭 
    
    # 方式2：一次性读取 使用list记录(生成二维list，一行在同一个数组中)
    exampleData = list(csvReader)
    print("exampleData ...")
    print(exampleData)

    # 遍历一次性记录CSV的exampleData
    for idx, row in enumerate(exampleData):
        #print(type(row)) #list
        print('Row #' + str(idx) + ' ' + str(row))
    
    
# csv.writer(csvfileObj): Write csv  二维数组写入CSV文件
with open('example1.csv', 'w', newline='') as fw: #  for Windows
    a=csv.writer(fw, delimiter=',') #delimiter=',' 时，自动将list的每个数据写入在单个单元格中
    # , \t between cells in a row ;每个数据以;区分
    #写入的list数据每个数据以delimiter=xx隔开
    #delimiter=',' 时，自动将list的每个数据写入在单个单元格中
    for row in exampleData: #按行写入 一行写入一个单元格
        print(type(row))
        a.writerow(row) 
   
    
fw.close()
print('Done')