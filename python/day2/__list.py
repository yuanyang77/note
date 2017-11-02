#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:yancy

names = ["yy","yancy","中国","袁阳","yelan",["yelan","yuyang"],"linshan","linfan"]
names2 = [1,2,3,4]



#add
names.append("linshan")         #追加
names.insert(1,"你好")           #插入
names.append(("yy"))

#cheng
names[2] = "yyyyyy"




#select
print(names[0],names[2])
print(names[1:3])
print(names[3])
print(names[-3:-1])
print(names.index("中国"))
print(names.count("yy"))


#delete
names.remove("yy")
del names[1]
names.pop(1)



print(names2)

names.reverse()
print(names)
names2.clear()
print(names2)

# names.sort()
print(names)
names.extend(names2)
print(names)

import copy
names3 = names.copy()
names3 = copy.deepcopy(names)
print(names)
print(names3)
names[0] = "袁阳"
print(names)
print(names3)

# names[5][0] = "叶兰"
# print (names)
# print (names3)

