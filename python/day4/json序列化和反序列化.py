#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
import json

#json序列化
info = {
    'name':'yy',
    'age':22
}

f = open("test2.txt",'w')
print(json.dumps(info))
f.write(json.dumps(info))
f.close()


#json反序列化
f = open('test2.txt','r')
data = json.loads(f.read())
print(data['age'])


