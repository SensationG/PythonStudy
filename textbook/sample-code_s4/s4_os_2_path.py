import os
# -----------------文件路径处理/切割/解析/档案大小-----------
#os.path.realpath() - 绝对路径
print('1.返回当前工作目录：',os.getcwd()) 
print('2.返回绝对路径：',os.path.realpath('.')) #疑问？为什么加点
#realpath是脚本所在的绝对路径，os.getcwd()是工作目录，默认情况下是一样的，但是把当前工作工作区修改后，输出就不一样了。

# convert a relative path to an absolute filename, use abspath().
if not os.path.exists('test1'): #检查档案目录是否存在
    os.mkdir('test1') #不在则创建
print('3.abspath:',os.path.abspath('./test1')) #打印绝对路径

# =============================================================================
# os.path.abspath和os.path.realpath区别
# 1.都会返回文件的绝对路径
# 2.realpath会得到指向文件的路径（软链接）
# =============================================================================

curDir = os.getcwd()    
# os.path.join()：将多个路径组合后返回
print('4.组合路径：',os.path.join(curDir, 'test', 'myfile.py'))
print(os.path.join(curDir, '/test', 'myfile.py')) # / 从文件根目录开始组合

#os.path.expanduser('~'):  get the current user's home directory 
print('5.获取当前windows用户主目录:',os.path.expanduser('~'))#获取当前windows用户主目录
pathname = os.path.join(os.path.expanduser('~'), 'test', 'myfile.py')
print('pathname-->',pathname)


#os.path.split(): split full pathnames, directory names, and filenames into their constituent parts.
dirname, filename = os.path.split(pathname) #切割路径名pathname 为路径+文件名
print("6.路径分割os.path.split() ...") #切割路径 分为 路径+档名
print("dirname", "=>", dirname) 
print("filename", "=>",filename)
print()
#*****************************
# os.path.dirname(), os.path.basename() 使用方法获取 上级路径+文件名
print("os.path.dirname(), os.path.basename()...")
print ("dirname", "=>", os.path.dirname(pathname))
print ("basename", "=>", os.path.basename(pathname))
print ("join", "=>", os.path.join(os.path.dirname(pathname),
                                 os.path.basename(pathname)))

# os.path.splittext(): splits a filename into a tuple containing the filename and the file extension
(shortname, extension) = os.path.splitext(filename) #文件名称拆解 name+后缀
print(shortname) #档案name
print(extension) #档案后缀

# os.path.getsize(): checking file size
print(os.path.getsize("C:\\Windows\\System32\\adsnt.dll")) #档案大小




