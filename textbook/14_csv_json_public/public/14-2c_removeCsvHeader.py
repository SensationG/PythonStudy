#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the data directory.

#--------------读取CSV 去除标题*（第一行）后 将剩下内容写入新的CSV中-----------
import csv
import os

data_dir = 'removeCsvHeaderData'
target_dir = os.path.join(data_dir, 'headerRemoved')

os.makedirs(target_dir, exist_ok=True) #新建文件夹

# 遍历data_dir文件夹下的每个文件
for filename in os.listdir(data_dir):
    #1 判断是否为CSV文件
    if not filename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + filename + '...')

    # Read the CSV file with skipping first row
    csv_rows = []
    # Note: csv files 在 data_dir
    #2 组合当前文件的路径 打开文件
    csvfile = open(os.path.join(data_dir, filename))
    #3 读取该csv内容
    csv_reader = csv.reader(csvfile)
    next(csv_reader) # skip first row 跳過第一列
    #4 将除了第一列的所有内容写入list 
    for row in csv_reader:
        #if csv_reader.line_num == 1:
        #    continue # skip first row
        csv_rows.append(row)
    csvfile.close()
    
    #use any to check if any column in the row contains data
    #    if any([x.strip() for x in row]):
    #5 将list中的内容写出到csv
    #  遇到写入时list数据直接会空一格的问题 使用newline=''
    with open(os.path.join(target_dir, filename), 'w', newline='') as f:
        csv_writer = csv.writer(f)#默认delimiter=',' 写入每个单元格中
        for row in csv_rows:
            csv_writer.writerow(row)
    f.close()
