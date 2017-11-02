#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:yancy

list_1 = [1,3,4,2,1,1,4,5,7,8,9]
list_1 =  set(list_1)                   #定义一个集合，集合天去重，不会有重复的元素
print(list_1,type(list_1))

list_2 = set([2,3,1,3,10,7,444,333])
print(list_1,list_2)

#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)

#并集
print(list_1.union((list_2)))
print(list_1 | list_2)

#差集   一个里面有，另一个里面没有的集
print(list_1.difference(list_2))    #in list_1 but not in list_2
print(list_2.difference(list_1))    #in list_2 but not in list_1
print(list_1 - list_2)              ##in list_1 but not in list_2


#子集
list_3 = set([1,2])

print(list_1.issubset(list_2))      #list_1是不是list_2的子集,返回为False
print(list_1.issuperset(list_2))    #list_1是不是list_2的父集,返回为False

print(list_3.issubset(list_1))      #list_3是不是list_1的子集,返回为True
print(list_1.issuperset(list_3))    #list_1是不是list_3的父集,返回为True

#对称差集   去掉两个集合中的交集后，即去除大家都有的数据，保留一个月，另一个没有的数据。
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)

#增
list_1.add(777)     #在list_1中添加777
print(list_1)
list_1.update([100,200,300])    #添加多个元素
print(list_1)

#查
# 100 in list_1           #判断100在不在list_1这个集合里
# 200 not in list_1       #判断200是不是不在list_1这个集合里
print(len(list_1))         #查询列表长度

#改
list_1.copy()     #浅复制

#删
list_1.remove(100)          #删除指定的元素
print(list_1,"-----")
print(list_1.pop())         #随即删除一个元素，并返回删除的元素
list_1.discard(77)          #discard删除，有就删除，没有也不会报错