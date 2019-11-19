#!/usr/bin/python3

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

for row in rows:
    sheet.append(row)

# Create a REference object that refers to the numbers of golden medals    
data = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=6)

# Create category axises as text labels representing names of countries.
categs = Reference(sheet, min_col=1, min_row=1, max_row=6)

# Create a bar chart and set it data and categories.
chart = BarChart()
chart.add_data(data)
chart.set_categories(categs)

# Turn off the legends and major grid lines
chart.legend = None
chart.y_axis.majorGridlines = None

# Let each bar has a different colour.
chart.varyColors = True

# Set chart's title
chart.title = "Olympic Gold medals in London"

sheet.add_chart(chart, "D2")

book.save("barChart.xlsx")