# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:25:10 2019

@author: hhw
"""

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 11): #可以附加行，从第一列开始附加
    sheet.append([i])
    
wb.save('hha.xlsx')