# Adding a second axis actually involves creating a second chart 
# that shares a common x-axis with the first chart but has a separate y-axis.
#------------------------横向绘图-绘制双y轴 直方图+折线图-----------------
from openpyxl import Workbook
from openpyxl.chart import (
    LineChart,
    BarChart,
    Reference,
    Series,
)

wb = Workbook()
ws = wb.active

rows = [ #二维list
    ['Aliens', 2, 3, 4, 5, 6, 7],
    ['Humans', 10, 40, 50, 20, 10, 50],
]

for row in rows:
    ws.append(row)
# 1 绘制第一个图
c1 = BarChart()
v1 = Reference(ws, min_col=1, min_row=1, max_col=7)#数据源
#当你的数据源包含title时，需要titles_from_data=True 这样绘制的数据会避免将title绘入
#当需要使用行为数据源（y轴），列为x轴时，需要设定from_rows=True
c1.add_data(v1, titles_from_data=True, from_rows=True)

c1.x_axis.title = 'Days'
c1.y_axis.title = 'Aliens'
c1.y_axis.majorGridlines = None
c1.title = 'Survey results'

# 2 绘制第二个图
c2 = LineChart()
v2 = Reference(ws, min_col=1, min_row=2, max_col=7)
c2.add_data(v2, titles_from_data=True, from_rows=True)
c2.y_axis.axId = 500 #设定右侧y轴的显示刻度 （没有发现数字的区别 估计仅代表代号
c2.y_axis.title = "Humans" #右侧y轴的标题
#c2.y_axis.majorGridlines = None

# Display y-axis of the second chart on the right by setting it to cross the x-axis at its maximum
# 3 将第二张图表的y轴设置为与x轴最大交叉，以显示其右边的y轴
c2.y_axis.crosses = "max"
c1 += c2 

ws.add_chart(c1, "D4")

wb.save("comboChart.xlsx")