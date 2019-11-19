# OS functions

import os

# Get the users environment 
#print(os.environ)
#--------------------------文件目录获取/创建/更改文件名----------------

# os.getcwd(): 返回当前工作目录
curDir = os.getcwd()
#print(curDir)

# os.listdir(path): 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
dirs=os.listdir(curDir)
#for file in dirs:
    #print(file)

# os.chdir(path): 切换目录到..
#os.chdir('../00 Misc/')

# os.mkdir(path): 新建文件夹并指定名称 当文件存在会报错
os.rmdir('newDir')  #删除文件夹
os.mkdir('newDir')  #创建文件夹

# os.rename(src, dst): 更改文件名称
os.rename('3.txt','3.txt')

# os.rmdir(path): 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError
#os.rmdir('newDir2')

# os.makedirs(path): 创建递归目录
os.makedirs('test1\\test11\\test111')

#os.removedirs(path): 删除递归目录
os.removedirs('test1\\test11\\test111')

# os.remove(path): 删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。


