#! python3
# readCensusExcel.py - Tabulates population and number of census tracts (areas) for 
# each county.
#----------------------------------存疑 从excel读取并写入文本文档--------------

import openpyxl, pprint
print('Opening workbook...')

# Loading workbook
wb = openpyxl.load_workbook('censuspopdata.xlsx')

#sheet = wb.get_sheet_by_name('Population by Census Tract')
sheet = wb['Population by Census Tract']

countyData = {} # (state：{county：{'tracts': 0, 'pop': 0}})

# Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1): #遍历excel 第二行到最大行
    # Each row in the spreadsheet has data for one census tract.
    # 赋值 按列赋值
    state  = sheet['B' + str(row)].value 
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value

    # 如果键不存在于字典中，将会添加键并将值设为默认值 ‘state’
    countyData.setdefault(state, {}) 
    # Make sure the key for this county in this state exists.设置默认值
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.txt', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
