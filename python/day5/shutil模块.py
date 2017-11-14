#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
import shutil
#  该模块可以处理高级的 文件、文件夹、压缩包
def copyfileobj(fsrc,fdst,length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

f_1 = open("file1","r+",encoding="utf-8")
f_2 = open("file2","a+",encoding="utf-8")   #如果这里是“r+”的方式打开的话那么在下面调用copyfileobj函数的时候，这个文件会被重定向的哟！（也就是之前的内容会被覆盖掉）
shutil.copyfileobj(f_1,f_2)     #将f_1文件的内容追加到f_2文件中.



# http://www.cnblogs.com/yinzhengjie/p/6428006.html


for thief in ['a','b','c','d']:
    sum = (thief != 'a') + (thief == 'c') + (thief == 'd') + (thief !='d')
    if sum == 3:
        print ("小偷是：%s " % thief)