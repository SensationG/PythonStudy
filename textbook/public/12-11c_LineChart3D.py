from datetime import date

from openpyxl import Workbook
from openpyxl.chart import (
    LineChart3D,
    Reference,
)
from openpyxl.chart.axis import DateAxis

wb = Workbook()
ws = wb.active

rows = [
    ['Date', 'Batch 1', 'Batch 2', 'Batch 3'],
    [date(2015,9, 1), 40, 30, 25],
    [date(2015,9, 2), 40, 25, 30],
    [date(2015,9, 3), 80, 30, 45],
    [date(2015,9, 4), 30, 25, 40],
    [date(2015,9, 5), 25, 35, 30],
    [date(2015,9, 6), 20, 40, 35],
]

for row in rows:
    ws.append(row)

c1 = LineChart3D()
c1.title = "3D Line Chart"
c1.legend = None
c1.style = 26
c1.y_axis.title = 'Size'
c1.x_axis.title = 'Test Number'
c1.varyColors = True

data = Reference(ws, min_col=2, min_row=1, max_col=4, max_row=7)
labels = Reference(ws, min_col=1, min_row=2, max_col=1, max_row=7)

c1.add_data(data, titles_from_data=True)
c1.set_categories(labels)

ws.add_chart(c1, "F2")

wb.save("lineChart3D.xlsx")