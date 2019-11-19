# coding='utf-8'

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

# get first row
first_row = list(sheet.rows)[0]

# values in first row
print("First row:")
for c in first_row:
    print(c.value, end= ' ')
print("\n")
    
# Read data row by row
print("Data row by row:")
for row in sheet.iter_rows(min_row=1, min_col=1, max_row=6, max_col=3):
    #print(row)
    data = []
    #data = [cell.value for cell in row]
    for cell in row:
        print(cell.value, end=" ")
        data.append(cell.value)
    print(" --> data in list:", data)
    print()
    
book.save('append_values.xlsx')