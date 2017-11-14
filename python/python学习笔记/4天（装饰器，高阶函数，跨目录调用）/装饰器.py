#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
# 装饰器：本质是函数，（装饰其他函数）,为其他函数添加附加功能
# 原则:装饰器对它被装饰的函数是完全透明的,大致分为两个特色：
#     1.不能修改被装饰的函数的原代码
#     2.不能修改被装饰的函数的调用方式

# 1.函数即"变量"
# 2.高阶函数
#     a：把一个函数名当做实参传给另一个函数 (在不修改被装饰函数的源代码的情况下为其添加功能)
#     b：返回值中包含函数名 (不修改函数的调用方式)
# 3.嵌套函数
# 高阶函数+嵌套函数 -->> 装饰器
