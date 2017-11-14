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
