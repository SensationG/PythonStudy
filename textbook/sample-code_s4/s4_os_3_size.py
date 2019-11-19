import os

#---------------统计指定文件夹内的所有文件大小----------------

totalSize = 0
pathname = 'C:\\Windows\\System32'

for filename in os.listdir(pathname):#返回指定的文件夹包含的文件或文件夹的名字的列表。
    totalSize = totalSize + os.path.getsize(os.path.join(pathname, filename))

print(pathname + " has " + str(totalSize/10**6) + " Mbytes.")