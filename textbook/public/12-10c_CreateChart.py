# CreateChart.py
"""
http://zetcode.com/articles/openpyxl/

1. Create a Reference object from a rectangular selection of cells.  
2. Create a Chart object.
3. Add the data series referred by the Reference object to the Chart object. 
4. Optionally, set ttitle and legend of the Chart object. 
5. Add the Chart object to the Worksheet object.
"""

import openpyxl
from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 11):
    sheet.append([i])

for i in range(1, 11):          # create some data in column A        
    sheet['A' + str(i)] = i

# Data series is a reference to cell ranges
data = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

# Create a barChart
chart = BarChart()

# Add the data series to the chart
chart.add_data(data)

# set the chart's title and legend
chart.title = "Sample BarChart"
chart.x_axis.title = 'Rank'
chart.y_axis.title = 'Value'
chart.legend = None

# anchor the top-lfet corner of chart at E2
sheet.add_chart(chart, "E2")

wb.save("SampleChart.xlsx")