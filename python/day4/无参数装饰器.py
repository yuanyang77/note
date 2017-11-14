#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
import time
#定义一个装饰器，实现统计每个函数的运行时间
def timmer(func): #定义一个装饰器名称（也可以理解定义一个变量），并定义一个需要装饰的参数，当调用的时候必须将被装饰的参数替换，Python默认做了这个操作
    def warpper(*args,**kwargs):  #这个就是装饰器，里面会存着传给func的参数
        start_time = time.time()
        res = func(*args,**kwargs) #运行被装饰的函数
        stop_time = time.time()
        print('the func tun time is %s' % (stop_time - start_time))
        return res
    return warpper

# 定义一个函数,并且使用@符号调用装饰器即可！
@timmer  #相当于test1 = timer(test1) 这个时候会去调用timmer这个装饰器。
def test1():#这个功能只是打印字符串的功能
    time.sleep(3)
    print("in the test1")

@timmer #相当于test2 = timer(test2)
def test2(name,age):#这个功能只是打印字符串的功能，并且还有返回值
    time.sleep(3)
    print("My name is \033[32;1m%s:\033[0m" % name)
    print("My age is \033[32;1m%s:\033[0m" % age)
    return 100

# 调用对应的函数
result_1= test1()
result_2 = test2("yancy",25)
print(result_1)
print(result_2)


#以上代码执行效果如下：
'''
in the test1
the func tun time is 3.000213146209717
My name is yancy:
My age is 25:
the func tun time is 3.0001907348632812
None
100
'''
