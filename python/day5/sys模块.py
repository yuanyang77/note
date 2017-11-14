import sys

# #1.获取Python解释程序的版本信息
print(sys.version)

#2.返回操作系统平台名称
print(sys.platform)

#3.返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path)

#4.退出程序，正常退出时exit(0),如果不写数字的话，默认就是0
print(sys.exit(7))

#5.命令行参数List，第一个元素是程序本身路径，运行的时候可以给脚本传递参数，就像shell的$1 $2一样。
a = sys.argv[1]
print(a)

#6.显示当前系统最大的Int值
print(sys.maxsize)

# 更多使用方法请参考：https://docs.python.org/2/library/sys.html?highlight=sys#module-sys