#! python3
# adjustCellHeightWidth.py - Adjust cell's height and width
#------------------------调整单元格大小------------------------
import openpyxl
  
wb = openpyxl.Workbook()

# get active sheet
sheet = wb.active

sheet['A1'] = 'Tall row'
sheet['B2'] = 'Wide column'

# set the height of the row  调整高度
sheet.row_dimensions[1].height = 90 #第一排的高度
  
# set the width of the column  调整宽度
sheet.column_dimensions['B'].width = 20 #B列宽度

wb.save('dimensions.xlsx')


#-----------测试--------------
wb2 = openpyxl.load_workbook('dimensions.xlsx') #打开
sheet = wb2.active

sheet['C1'] = 'aaaa'
sheet['C3'] = 'qweqwe'

sheet.row_dimensions[1].height = 30
sheet.column_dimensions['C'].width = 40

wb2.save('dimensions.xlsx')