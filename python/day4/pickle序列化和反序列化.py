#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
#pickle序列化
import pickle
def sayhi(name):
    print("hello",name)

info = {
    'name':'yy',
    'age':22,
    'func':sayhi
}

f = open("test2.txt",'wb')
print()
f.write(pickle.dumps(info))
f.close()


#pickle反序列化
def sayhi(name):
    print("hello2",name)

f = open("test2.txt",'rb')
data = pickle.loads(f.read())

print(data['func']("yancy"))