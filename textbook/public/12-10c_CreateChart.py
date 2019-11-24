# CreateChart.py
"""
http://zetcode.com/articles/openpyxl/

1. Create a Reference object from a rectangular selection of cells.  
2. Create a Chart object.
3. Add the data series referred by the Reference object to the Chart object. 
4. Optionally, set ttitle and legend of the Chart object. 
5. Add the Chart object to the Worksheet object.
"""
#------------------------------excel画基础柱状图BarChart--------------------------
import openpyxl
from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()
sheet = wb.active

# 添加数据 2种方式
for i in range(1, 11): # 方式一 append
    sheet.append([i])

for i in range(1, 11):  #方式二 
    sheet['A' + str(i)] = i

# 1 设定要绘图数据 这里只设置y轴的数据
    #只设置了y轴的数据时，x轴默认为行名
data = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
#labels = Reference(ws, min_col=1, min_row=2, max_col=1, max_row=7)添加x轴数据

# 2 Create a barChart 创建图表
chart = BarChart()

# 3 Add the data series to the chart
chart.add_data(data)
#chart.set_categories(labels) #添加x轴数据

# 4 set the chart's title and legend #设定画图参数
chart.title = "Sample BarChart" #图表名称
chart.x_axis.title = 'Rank'    #x轴名称
chart.y_axis.title = 'Value'   #y轴名称
chart.legend = None    

# 5 anchor the top-lfet corner of chart at E2 图放的位置
sheet.add_chart(chart, "E2")


wb.save("SampleChart.xlsx")