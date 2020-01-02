import csv

#----------------使用next读取（标题）下一行资料---------------

# Read csv

with open('AQI_20191101.csv', encoding='utf-8') as f:

    # csv.reader(f): read from csv file
    csv_reader = csv.reader(f, delimiter=',')

    headers = next(csv_reader)#使用next来读取下一行的资料

    # Remove 'utf-8-sig' BOM
    headers = [s.replace("\uFEFF", "") for s in headers]
    print(headers[0:5])
    
    for row in csv_reader: #因为上面使用了next，所以打印的是接next之后的资料
        print(row[0:5])

f.close()
print('Done')