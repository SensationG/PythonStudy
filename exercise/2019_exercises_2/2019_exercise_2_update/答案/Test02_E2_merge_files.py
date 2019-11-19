"""Open a file with correct encoding"""

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

# Find file, dir and data paths
filepath = os.path.abspath(__file__)
dirpath =  os.path.dirname(filepath)
datapath = os.path.join(dirpath, 'data')
outfile = os.path.join(dirpath, "files", "merged.txt")

ext_list = ['.txt', '.csv'] # 欲處理的副檔名清單

# Loop over the files in the datapath directory

with open(outfile, 'w+', encoding='utf=8') as writer:
  # 轉換 os.listdir() 回傳的項目為完全路徑
  files = [os.path.join(datapath, f) for f in os.listdir(datapath)]
  for fn in files:
    #if fn.endswith('txt') or fn.endswith('csv'):
    ext = os.path.splitext(fn)[1] # 取得副檔名
    if ext in ext_list:
      fn_encoding = predict_encoding(fn)
      print("%s encoded in %s\n" % (os.path.basename(fn), fn_encoding))
      
      if not fn_encoding or fn_encoding in ['Big5', 'cp950', 'ISO-8859-1']:
        fn_encoding = None # use windows default
    
      with open(fn, "r", encoding=fn_encoding) as f:
        #lines = f.readlines()
        #for l in lines:
        for l in f:
          writer.write(l)
      writer.write('\n')
      f.close()
      
writer.close()

"""
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]
"""