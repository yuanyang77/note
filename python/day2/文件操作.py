#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
#data = open("yesterday",encoding="utf-8").read()   #读取文件内容
# print(data)

f = open("yesterday",encoding="utf-8")       #文件句柄
# f.read()
data = f.read()
data2 = f.read()
print(data)
print()
