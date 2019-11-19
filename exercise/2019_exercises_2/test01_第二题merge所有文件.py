"""Open a file with correct encoding"""

import os

def predict_encoding(file_path): ## 自动检测字符集编码
  '''Predict a file's encoding using chardet'''
  import chardet
  import os
  encoding = ''
  bytes = min(1024, os.path.getsize(file_path))

  # Open the file as binary data
  raw = open(file_path, 'rb').read(bytes)

  result = chardet.detect(raw)
  encoding = result['encoding']

  return encoding


filepath = os.path.abspath('credits.txt')#文件所在的路径 
dirpath = os.path.dirname(filepath) #文件所在的目录（不包括文件本身）
datapath = os.path.join(dirpath,'data') #该文件下的data文件夹
outpath = os.path.join(datapath,'review','merged.txt')#合并后存储的文件路径

ext_list = ['.txt', '.csv'] # 欲處理的副檔名清單

with open(outpath, 'w+', encoding='utf=8') as writer:
    files=[os.path.join(datapath,f) for f in os.listdir(datapath)]#遍历该目录下的所有文件并合并路径
    i=0
    for filename in files: #遍历文件路径      
      #if filename.endswith('txt') or filename.endswith('csv'): 检查文件类型是否匹配 
      ext = os.path.splitext(filename)[1] # 取得文件后缀名
      if ext in ext_list: #如果匹配文件后缀名清单 则开始写入
        f_encoding = predict_encoding(filename) #返回文件编码 
        print(filename, "encoded in", f_encoding)
        i+=1
    
        with open(filename, "r", encoding=f_encoding) as f:  #打开文件并记录
          for line in f:    #按行读取并打开
             writer.write(line) #文件写入
        writer.write('\n')
        f.close()
           

print(i)#文件数量统计
