import csv

# Read csv 文件打不开 CSV的读取与写入
data_rows = [] # empty data rows

with open('grades1.csv') as csvfile:

    # csv.reader(csvfile): read from csv file
    csv_reader = csv.reader(csvfile, delimiter=',')

    # 一行一行讀取 csv reader 物件的內容，並轉換成 陣列
    #for idx, row in enumerate(csv_reader):
    #    print('Row #' + str(idx) + ' ' + str(row))
    # csv.reader 物件已到盡頭 
    # 取得欄位標題
    headers = next(csv_reader)
    headers.append('平均成績')
    
    for i, row in enumerate(csv_reader):
      # 確認成績欄位都是整數 row = [學號] + [成績串列]
      row = [row[0]] + [int(c) for c in row[1:]]
      avg = round(sum(row[1:])/len(row[1:]), 2)
      row.append(avg)
      data_rows.append(row)

# csv.writer(f): Write csv   写入CSV
with open('grades_avg.csv', 'w', newline='') as fw: # for Windows
    writer = csv.writer(fw, delimiter=',')          # , 
    writer.writerow(headers)                        # 先加入欄位標題列

    for row in data_rows:
        writer.writerow(row)

fw.close()
print('Done')