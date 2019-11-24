import openpyxl
from openpyxl.chart import BarChart, Reference, Series

#---------------------绘制多数据柱状图-------------并带有图例

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 11): # create some data in column A
    sheet['A' + str(i)] = i+2

for i in range(1, 11): # 测试 添加第二个数据
    sheet['B' + str(i)] = i+3

#设置数据1
refObj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
seriesObj = Series(refObj, title='First series') #title为图例名称
#设置数据2
refObj2 = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=10)
seriesObj2 = Series(refObj2, title='Second series')

chartObj = BarChart()
chartObj.append(seriesObj) #添加数据1
chartObj.append(seriesObj2) #添加数据2

chartObj.title = "Sample BarChart"
chartObj.x_axis.title = 'Rank'
chartObj.y_axis.title = 'Value'

sheet.add_chart(chartObj, 'E2')
wb.save('sampleChart.xlsx')