# FreezePanes.py: freeze rows on top and columns to the left

import openpyxl
 
wb = openpyxl.load_workbook('produceSales.xlsx')
 
sheet = wb.active
 
sheet.freeze_panes = 'A2' # Freeze row 1

#sheet.freeze_panes = 'C2' # Freeze Row 1 and columns A and B 
#sheet.freeze_panes = None # or 'A1'

wb.save('freezeExample.xlsx')
