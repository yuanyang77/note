#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy

#小复习
# print('yuanyang'.replace('a','A',2))
# print('linfan'.replace("linfan","yy"))


#栗子一：
# f = open("filetest","r",encoding="utf-8")
# f_new = open("filetest.back","w",encoding="utf-8")
#
# for line in f:
#     if  "当我年少轻狂" in line:
#         line = line.replace("当我年少轻狂","我当时年少轻狂")
#     f_new.write(line)
# f.close()
# f_new.close()

# 栗子二：
#使用传参的方式替换
#sys.argv函数相当shell里的 $1  $2的这种用法
# import sys
# f = open('filetest','r',encoding="utf-8")
# f_new = open('filetest.back','w',encoding="utf-8")
# find_str = sys.argv[1]
# replace_str = sys.argv[2]
#
# for line in f:
#     if find_str in line:
#         line = line.replace(find_str,replace_str)
#     f_new.write(line)
# f.close()
# f_new.close()

# 栗子三：
#使用传参的方式替换.使用with函数来打开多个文件，避免忘记关闭文件，内存被爆的惨剧
import sys
find_str = sys.argv[1]
replace_str = sys.argv[2]
with open('filetest','r',encoding="utf-8") as f1, \
     open('filetest.back','w',encoding="utf-8") as f2:  #python的代码规范要求每行最多不要超过80个字符，所以如果一行过长，应该尽量使用 \ 换行成多行，方便阅读。
    for line in f1:
        if find_str in line:
            line = line.replace(find_str,replace_str)
        f2.write(line)
    print(f1.readline())

