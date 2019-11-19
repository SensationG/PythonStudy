import openpyxl
from openpyxl.chart import BarChart, Reference, Series

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 11): # create some data in column A
    sheet['A' + str(i)] = i

refObj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
seriesObj = Series(refObj, title='First series')

chartObj = BarChart()
chartObj.append(seriesObj)

chartObj.title = "Sample BarChart"
chartObj.x_axis.title = 'Rank'
chartObj.y_axis.title = 'Value'

sheet.add_chart(chartObj, 'E2')
wb.save('sampleChart.xlsx')