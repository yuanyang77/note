#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
# 时间模块
# 时间戳格式：
# 格式化字符串(tuple)格式：
# 格式化字符串格式：

import time
# print(time.time())              #获取时间戳
# # time.sleep(3)                   #睡眠3s
# print(time.localtime())         #获取格式化字符串(tuple)格式
#
# print(time.timezone)            #获取本地时区
# print(time.altzone)             #
# print(time.daylight)
#
# x = time.localtime(1234567890)
# print(x)
# print(x.tm_year)
# print('this is 2009 day:%d' %x.tm_yday)
#
# print(x)
# print(time.mktime(x))
#
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(time.strftime("%Y-%m-%d %H:%M:%S"),x)

# print(time.strptime('2017-11-13 10:37:40',"%Y-%m-%d %H:%M:%S"))
#
# print(time.asctime())
# print(time.ctime(1503123587))

import datetime
print(datetime.date)
print(datetime.datetime)
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(3))
print(datetime.datetime.now()+datetime.timedelta(hours = 3))
print(datetime.datetime.now()+datetime.timedelta(hours = -3))

import random
checkcode=""
for i in range(4):
    current=random.randrange(0,4)
    if current ==i:
        tmp=chr(random.randint(65,90))
    else:
        tmp=random.randint(0,9)
    checkcode+=str(tmp)
print(checkcode)

