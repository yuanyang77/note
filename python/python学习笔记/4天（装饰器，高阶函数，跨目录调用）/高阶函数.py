#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
def bar():
    print("in the bar")

def test1(func):
    print(func)
    func()
test1(bar)

import time

# 1.把一个函数名当作实参传给另外一个函数(在不修改被装饰函数源代码的情况下为其添加附加功能);
def test1(fun):
    start_time = time.time()
    fun()
    stop_time= time.time()
    print("the fun run time is %s" %(stop_time-start_time))

def bar():
    print("in the bar")
    time.sleep(3)
test1(bar)

# 2.返回值中包含函数名(不修改函数的调用方式)。
import time
def bar():
    time.sleep(3)
    print('in the bar')
def test2(func):
    print(func)
    return func

# print(test2(bar))
bar=test2(bar)
bar()  #run bar