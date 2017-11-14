#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
''''
  导入模块：
	import module_name
	import module_name,modelue2_name
	from module_name import *   (尽量不要使用)
	from module_name import m1,m2,m3
	from module_name import as module_name_alias
    '''

import module_yy
print(module_yy.name)
print(module_yy.loger())

from module_yy import name
print(name)

from module_yy import *
print(word())

from module_yy import hello_yy
print(hello_yy())

from  module_yy import hello_yy as yy
print(yy())

import sys,os
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #获取上上一层的目录路径
x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))     #把路径赋值给一个变量
sys.path.append(x)      #把路径添加到环境变量的最后
sys.path.insert(0,x)    #把路径插入到环境变量的开头
print(x)
