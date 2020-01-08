import pandas as pd
import os
#-------------使用pandas excel转csv-----快速！--------------

xlfname = 'example.xlsx'
fname, ext = os.path.splitext(xlfname) 
xl = pd.ExcelFile(xlfname)
 
for sheet in xl.sheet_names:
    print(sheet)
    df = xl.parse(sheet) #将每个工作簿转成dataframe
    #df = pd.read_excel(xlfname, sheet) #直接读取excel内的指定分页
    csvfname = fname + '_'  + sheet + '.csv'
    df.to_csv(csvfname, encoding='utf-8', index=False)#输出csv文件