import openpyxl

from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']

fontObj1 = Font(name='微軟正黑體', bold=True)
#sheet['A1'] = 'Bold Times New Roman'
a = sheet['A1']
a.font = fontObj1
a.value = 'Bold 微軟正黑體 中文' # text for demonstration

fontObj2 = Font(name='Times New Roman', size=24, italic=True)
b = sheet['B3']
b.font = fontObj2
b.value = '24 pt Italic' # 展示用文字

wb.save('styles.xlsx')