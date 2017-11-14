#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy

#嵌套函数
def foo():
    print('in the foo')
    def bar():
        print('in the bar')

    bar()
foo()


x = 0
def grandpa():
    x = 1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)    #最终生效的作用域不是全局变量，而是当前函数的定义的变量x=3，这就是在嵌套函数中的作用域的功能！
        son()
    dad()
grandpa()

