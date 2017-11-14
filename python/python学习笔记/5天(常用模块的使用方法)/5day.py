1.定义
  模块：用来从逻辑上组织python代码（变量，函数，类，逻辑：实现一个功能），本质就是一个.py的python文件，（例如：test.py,对应的模块名为: test）
  包:用来从逻辑上组织模块的，本质就是一个目录（必须带有一个_init_.py的文件）

2.导入方法
  导入模块：
	import module_name
	import module_name,modelue2_name
	from module_name import *  (尽量不要使用)
	from module_name import m1,m2,m3
	from module_name import as module_name_alias
	import 导入执行的时候，需要加上module_name
	from 导入不需要加module_name
  导入包：


3.import本质（路径搜索和搜索路径） 
  导入模块的本质就是把python文件解释执行一遍
  导入包的本质，就是解释执行包下面的__init__.py的文件


4.导入优化
  from modele_name import func_name


5.模块分类
  a:标准库
  b:开源模块
  c:自定义模块


os模块：
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


sys模块：

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


time And datatime模块：

# 在Python中，通常有这几种方式来表示时间：1）时间戳 2）格式化的时间字符串 3）元组（struct_time）共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同。

# UTC（Coordinated Universal Time，世界协调时）亦即格林威治天文时间，世界标准时间。在中国为UTC+8。DST（Daylight Saving Time）即夏令时。

# 时间戳（timestamp）的方式：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。返回时间戳方式的函数主要有time()，clock()等。

# 元组（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。下面列出这种方式元组中的几个元素：

import time

#获取时间戳
print(time.time())

#睡眠3s
time.sleep(3)

# 返回处理器时间,3.3开始已废弃 , 改成了time.process_time()测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
print(time.clock())

#返回与utc时间的时间差,以秒计算\
print(time.altzone)

#返回时间格式"Mon Nov 13 23:03:10 2017"
print(time.asctime())

#返回本地时间 的struct time对象格式,获取格式化字符串(tuple)格式
print(time.localtime())
'''
返回：
“time.struct_time(tm_year=2017, tm_mon=11, tm_mday=13, tm_hour=23, tm_min=15, tm_sec=6, tm_wday=0, tm_yday=317, tm_isdst=0)”
'''

#返回utc时间的struc时间对象格式
print(time.gmtime(time.time()-70000))

#返回时间格式"Mon Nov 13 23:18:55 2017",
print(time.asctime(time.localtime()))

# 返回时间格式，同上
print(time.ctime())

# 将日期字符串转成struct时间对象格式
string_2_struct = time.strptime("2017/11/13","%Y/%m/%d")
print(string_2_struct)

# 将struct时间对象转成时间戳
struct_2_stamp = time.mktime(string_2_struct)
print(string_2_struct)

# 将utc时间戳转换成struct_time格式
print(time.gmtime(time.time()-86640))

#查看是否有使用夏令时，没有返回0，有的话返回夏令时的时区
print(time.daylight)

# 将utc struct_time格式转成指定的字符串格式
# print(time.strptime("%Y-%m-%d %H:%M:%S",time.gmtime()))

# 时间加减
import datetime     #返回  2017-11-13  年月日格式

print(datetime.datetime.now()) #返回 2017-11-13 23:28:49.249611
print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now() )
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分

c_time = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))  #时间替换


# 格式参照
# %a    本地（locale）简化星期名称
# %A    本地完整星期名称
# %b    本地简化月份名称
# %B    本地完整月份名称
# %c    本地相应的日期和时间表示
# %d    一个月中的第几天（01 - 31）
# %H    一天中的第几个小时（24小时制，00 - 23）
# %I    第几个小时（12小时制，01 - 12）
# %j    一年中的第几天（001 - 366）
# %m    月份（01 - 12）
# %M    分钟数（00 - 59）
# %p    本地am或者pm的相应符    一
# %S    秒（01 - 61）    二
# %U    一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。    三
# %w    一个星期中的第几天（0 - 6，0是星期天）    三
# %W    和%U基本相同，不同的是%W以星期一为一个星期的开始。
# %x    本地相应日期
# %X    本地相应时间
# %y    去掉世纪的年份（00 - 99）
# %Y    完整的年份
# %Z    时区的名字（如果不存在为空字符）
# %%    ‘%’字符

# http://egon09.blog.51cto.com/9161406/1840425


random模块：

import random

# 随机数
print(random.random)
print(random.randint(1,3))
print(random.randrange(1,10))

import random
checkcode = ""
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)


pickle & json:
# 用于序列化的两个模块
#
# json，用于字符串 和 python数据类型间进行转换
# pickle，用于python特有的类型 和 python的数据类型间进行转换
# 补充说明：将数据通过特殊的形式转换成只有python解释器识别的字符串，这个过程我们叫做序列化，而把哪些python能够识别的字符串转换成我们能看懂的叫做反序列化。
# Json模块提供了四个功能：dumps、dump、loads、load
#
# pickle模块提供了四个功能：dumps、dump、loads、load

#1.将数据通过特殊的形式转换为只有python语言知识的字符串并写入文件

import pickle,json
# pickle
#     1.>用于python特有的类型 和 python的数据类型间进行转换
#     2.>pickle模块提供了四个功能：dumps、dump、loads、load.
#     补充说明：将数据通过特殊的形式转换成只有python解释器识别的字符串，这个过程我们叫做序列化，而把哪些python能够识别的字符串转换成我们能看懂的叫做反序列化。
data = {"k1":123,"k2":'hello'}
p_str = pickle.dumps(data)
print(p_str)
f = open("test.txt","wb")
f.write(p_str)

#2.上面的写入文件的方法也可以这么玩,看起来更简单
with open("test.txt",'wb') as f:
    pickle.dump(p_str,f)


# 把存入文件的东西读出来
f = open("test.txt",'rb')
print(pickle.loads(f.read()))

f = open('test.txt','rb')
print(pickle.load(f))

# json
# 用于序列化的两个模块
#     1>.json:用于字符串 和 python数据类型间进行转换
#     2>.pickle:用于python特有的类型和python的数据类型间进行转换
#     json模块提供了四个功能：dumps、dump、loads、load
#     pickle模块提供了四个功能：dumps、dump、loads、load

#json.dump 把数据通过特殊形式转换为所有程序语言都认识的字符串，并写入文件
data = {"k1":123,"k2":'hello'}
j_str = json.dumps(data)
print(j_str)

with open("test2.txt",'w') as fp:
    json.dump(data,fp)


# 存数据方式一：
accounts = {'id':7,'name':'yy','age':25}
f = open("test2.txt","w")
json_str = json.dumps(accounts)
f.write(json_str)
# 存数据方式二：
with open("test2.txt","w") as fp:
     json.dump(accounts,fp)
# 读取数据的方法一：
f = open("test2.txt","r")
print(json.loads(f.read()))
# 方法二:
f = open("test2.txt","r")
print(json.load(f))