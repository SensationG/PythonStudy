# FreezePanes.py: freeze rows on top and columns to the left

#---------------------------锁定单元格--------------
#使得在使用滚动条时候永远保持在最前
import openpyxl
 
wb = openpyxl.load_workbook('produceSales.xlsx')
 
sheet = wb.active
 
sheet.freeze_panes = 'A2' # Freeze row 1 冻结（范围）左上方单元格
#在横向滑动excel时就会锁定单元格 

#sheet.freeze_panes = 'C2' # Freeze Row 1 and columns A and B 
#sheet.freeze_panes = None # or 'A1'

wb.save('freezeExample.xlsx')
