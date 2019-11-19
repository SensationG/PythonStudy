import openpyxl

# Creating a new workbook
wb = openpyxl.Workbook()
print(wb.sheetnames)

# Create one sheet
wb.create_sheet()

print("After creating one Sheet" )
print(wb.sheetnames)

print("After creating 'First Sheet' and 'Middle Sheet'" )
wb.create_sheet(index=0, title='First Sheet')
wb.create_sheet(index=2, title='Middle Sheet')

print(wb.sheetnames)

# remove_sheet() takes a Worksheet object, not a string of the sheet name, as its argument.
wb.remove(wb['Middle Sheet'])
wb.remove(wb['Sheet1'])
print("After removing 'Middle Sheet' and 'Sheet1'")
print(wb.sheetnames)

sheet = wb.active
print("active sheet:" + sheet.title)
sheet['A1'] = 'Hello'
print(sheet['A1'].value)