#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
#pickle序列化
import pickle
def sayhi(name):
    print("hello",name)

info = {
    'name':'yancy',
    'age':'25',
    'func':sayhi
}

f = open('test.text','wb')
pickle.dump(info,f)    #f.write( pickle.dumps( info) )
f.close()



import pickle

def sayhi(name):
    print("hello2,",name)

f = open("test.text","rb")


data = pickle.load(f) #data = pickle.loads(f.read())


print(data["func"]("yancy"))