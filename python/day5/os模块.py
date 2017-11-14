import os

#1.获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())

#2.改变当前脚本工作目录；相当于shell下cd,记住，这个是没有返回值
os.chdir(r"F:\note\python")
print(os.getcwd())

#3.返回当前目录: ('.')
print(os.curdir)

#4.获取当前目录的父目录字符串名：('..')
print(os.pardir)

#5.可生成多层递归目录(创建目录)
os.makedirs(r"F:\a\b\c\d\e")

#6.若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推（和上面的相反，就是删除目录。）
os.removedirs(r"F:\a\b\c\d\e")

#7.生成单级目录；相当于shell中mkdir dirname，如果当前目录已经存在改目录就会报错！
os.mkdir(r"F:\a")

#8.删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname,如果当前目录没有改目录就会报错！
os.rmdir(r"F:\a")

#9.列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
print(os.listdir(r"F:\note"))

# 10.删除一个文件
os.remove(r"F:\note\a.txt")

# 11.重命名文件/目录
os.rename(r"F:\note\test",r"F:\note\test2")

# 12.os.stat('path/filename')  获取文件/目录信息
print(os.stat(r"F:\\note"))

#13.输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.sep)

# 14.输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
print(os.linesep)

#15.输出用于分割文件路径的字符串
print(os.pathsep)

#16.输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.name)

#17.运行shell或者windows命令，直接显示命令的输出结果，可以将这个数据存放在一个变量中
print(os.system("dir"))
print(os.system("ls"))

#18.返回path的绝对路径
print(os.path.abspath(r"F:\note\README"))

#19.将path分割成目录和文件名二元组返回
print(os.path.split(r"F:\note\README"))

#20.返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname(r"F:\note\README"))

#21.os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.basename(r"F:\note\README"))

#22.os.path.exists(path) 判断path是否存在，如果path存在，返回True；如果path不存在，返回False
print(os.path.exists(r"D:\aaa"))
print(os.path.exists(r"F:\note\README"))

#23.os.path.isabs(path)  如果path是绝对路径，返回True
print(os.path.isabs(r"F:\note\README"))

#24.os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile(r"F:\note\README"))

#25.os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir(r"F:\note"))

#26.os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join(r"F:\note\README",r"F:\note\python",r"F:\note\shell"))

#27.os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
print(os.path.getatime(r"F:\note\README"))

#28.os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime(r"F:\note\README"))


# 更多关于os模块的使用方法请参考：https://docs.python.org/2/library/os.html?highlight=os#module-os

