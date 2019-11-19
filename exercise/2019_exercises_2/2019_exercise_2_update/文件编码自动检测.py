"""Open a file with correct encoding"""
# 检测字符集编码
import os

def predict_encoding(file_path):
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


# Loop over the files in the working directory.

#for filename in os.listdir('.'):#抓本目录底下的所有文件
#  if filename.endswith('txt') or filename.endswith('csv'):
#
#    print()
#    f_encoding = predict_encoding(filename)
#    print(filename, "encoded in", f_encoding)
#
#    if not f_encoding or f_encoding in ['Big5', 'cp950', 'ISO-8859-1']:
#      f_encoding = None # as default
#    
#    with open(filename, "r", encoding=f_encoding) as f:
#      for line in f:
#        print(line.strip('\n'))

a=predict_encoding('2019_Exercises_2.txt')  #返回文件的编码
print(a)
