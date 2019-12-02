# Check Path validility

#-------------------------检查文件/目录是否存在-------------------

import os

i=os.path.exists('C:\\Windows')##检查档案目录是否存在（不分檔案或目錄）
print(i) #返回true

os.path.exists('C:\\some_made_up_folder')

os.path.isdir('C:\\Windows\\System32') #isdir检查目录是否存在

os.path.isdir('C:\\Windows\\System32') ('C:\\Windows\\System32') #isfile检查文件是否存在

i=os.path.isdir('C:\\Windows\\System32\\calc.exe') 
print(i)

i=os.path.isfile('C:\\Windows\\System32\\calc.exe')
print(i)