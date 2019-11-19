#! python3
# updateProduce.py - Corrects costs in produce sales spreadsheet.

import openpyxl

wb = openpyxl.Workbook('')

sh = wb.active

sh['A1'] = 200
sh['A2'] = 300
sh['A3'] = '=SUM(A1:A2)'

wb.save('writeFormula.xlsx')

print(sh['A3'].value)

wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)

sh1 = wbDataOnly.active

#openpyxl doesn't evaluate formula, it returns None.
print(sh1['A3'].value)

