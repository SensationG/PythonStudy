# coding='utf-8'
#---------------------------使用append实现按行插入excel/按行读取------------------
from openpyxl import Workbook

book = Workbook()
sheet = book.active

rows = [
    [88, 46, '中文'],
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
]

# write data to sheet row by row
for row in rows:
    sheet.append(row)

# 1 get first row 按行读取数据 第一种方法
first_row = list(sheet.rows)[0]

# values in first row 打印第一行数据
print("First row:")
for c in first_row:
    print(c.value, end= ' ')
print("\n")
    
# 2 Read data row by row 按行读取数据 第二种方法
print("Data row by row:")#从第一行第一列到第六行第3列
for row in sheet.iter_rows(min_row=1, min_col=1, max_row=6, max_col=3):
    #print(row) 每行的数据
    data = []
    #data = [cell.value for cell in row]
    for cell in row: #每行的每个数据
        print(cell.value, end=" ")
        data.append(cell.value) #添加每行的每个数据
    print(" --> data in list:", data)
    print()
# 3 按行读取 第三种方法
for rows in sheet['A1':'C6']:
  for cellObj in rows:
    print(cellObj.value,end=' ')
    
  print()
    
book.save('append_values.xlsx')