#!/usr/bin/python3

#--------------绘制barChart直方图（多色）包括x轴数据+y轴数据 使用append插入单行-----------------
from openpyxl import Workbook
from openpyxl.chart import (
    Reference,
    Series,
    BarChart
)

book = Workbook()
sheet = book.active

# Create some data and add it to the cells of the active sheet.
rows = [
    ("USA", 46),
    ("China", 38),
    ("UK", 29),
    ("Russia", 22),
    ("South Korea", 13),
    ("Germany", 11)
]
#print(rows[0]) # ("USA", 46) 类型list
for row in rows: #list导入到excel
    sheet.append(row) #使用append每次插入一行

# Create a REference object that refers to the numbers of golden medals 设定y轴数据   
data = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=6)

# Create category axises as text labels representing names of countries.设定x轴数据
categs = Reference(sheet, min_col=1, min_row=1, max_row=6)

# Create a bar chart and set it data and categories.
chart = BarChart() #直方图类型
chart.add_data(data) #添加y轴数据
chart.set_categories(categs) #添加x轴数据

# Turn off the legends and major grid lines
chart.legend = None #图例设置为None
chart.y_axis.majorGridlines = None 

# Let each bar has a different colour. 設置顔色 彩色
chart.varyColors = True

# Set chart's title
chart.title = "Olympic Gold medals in London"

sheet.add_chart(chart, "D2")

book.save("barChart.xlsx")