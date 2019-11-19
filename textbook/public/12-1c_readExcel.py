import openpyxl

# Load in the workbook
wb = openpyxl.load_workbook('example.xlsx')

# Get sheet names
# wb.get_sheet_names()
print(wb.sheetnames)

# Get a sheet by name
# wb.get_sheet_by_name('Sheet3') 
sheet = wb['Sheet3']
print(sheet.title)

# # Get active sheet
# wb.get_active_sheet() 
sheet = wb.active
print("active sheet: " + sheet.title)

# Getting Cells from the Sheets
#print(dir(sheet))

# Retrieve the maximum amount of rows
# old: sheet.get_highest_row() 
# sheet.max_row

# Retrieve the maximum amount of columns
# old: sheet.get_highet_column() 
# sheet.max_column

print("This sheet has " + str(sheet.max_row) + ' rows ' + str(sheet.max_column) + ' columns.')

# Retrieve the value of a certain cell
print(sheet['A1'].value)

# Select element 'B1' of your sheet c = sheet["%s%d" % ("B", 1)]
c = sheet['B1']


print(c.value)  #'Apples'

print('Row ' + str(c.row) + ', Column ' + str(c.column) + ' is ' + c.value)

print('Cell ' + c.coordinate + ' is ' + c.value)
# 'Cell B1 is Apples'

# Print out odd rows' values in column 2 
for i in range(1, 8, 2):
  print(i, sheet.cell(row=i, column=2).value)

# Retrieve an range of cells
for rows in sheet['A1':'C3']:
  for cellObj in rows:
    print(cellObj.coordinate, cellObj.value)
  print('---- END OF ROW ----')
