#! python3
# adjustCellHeightWidth.py - Adjust cell's height and width

import openpyxl
 
wb = openpyxl.Workbook()

# get active sheet
sheet = wb.active

sheet['A1'] = 'Tall row'
sheet['B2'] = 'Wide column'

# set the height of the row 
sheet.row_dimensions[1].height = 90
  
# set the width of the column 
sheet.column_dimensions['B'].width = 20

wb.save('dimensions.xlsx')
