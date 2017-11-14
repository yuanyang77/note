#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
import time

def timer(func):    #timer(test1)   func=test1
    def deco(*args,**kwargs):
        star_time=time.time()
        func(*args,**kwargs)    #run test1()   run test2()
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-star_time))
    return deco



@timer      #test1 = timer(test1)
def test1():
    time.sleep(1)
    print('in the test1')

@timer      #test2 = timer(test2)
def test2(name,age):
    print('test2:',name,age)

test1()
test2('yancy',25)
