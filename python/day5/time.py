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

