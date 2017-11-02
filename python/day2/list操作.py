names = ["袁阳","中国","湖北","襄阳"]

#查
print(names)    #取值整个列表
print(names.index("湖北"))    #查找出列表中的某个值所对应的索引ID
print(names[names.index("襄阳")])     #根据列表中的索引ID返回所对应的值
print(names[0])     #取值第一个索引
print(names[0],names[3])    #取出第一个索引和第四个索引
print(names[1:3])           #从第二个索引开始取值，到第三个结束，切片不包含最后一个元素，俗称顾头不顾尾
print(names[-1])            #取切片取值最后一个值,即倒着取
print(names[-3:-1])         #从倒数第三个开始取值，取到最后一个值。该切片同样不包含最后一个元素
print(names[-3:])           #从倒数第三个数值开始取值，取到最后一个结束

#增
names.append("叶兰")         #追加一个新的值，也就是插入末尾
print(names)
names.insert(1,"深圳")        #在列表的第一个索引处插入一个新的值，前面的数字表示索引的位置，后面是对应该索引的值
print(names)

#删
names.remove("叶兰")          #删除值为"叶兰"的值
print(names)
del names[1]                #删除列表中第二个索引所对应的值
print(names)
names.pop()                 #如果不加数字，默认删除最后一个数值
print(names)
names.pop(1)                #删除第二个索引的值
print(names)
names.clear()               #清空列表
print(names)
# del names                   #删除整个列表


numbers = [0,1,2,3,4,5,6,7,8,9,"!","yancy","yy","yuanyang","yelan"]
print(numbers)
numbers.reverse()            #反转列表,就是讲列表的初始顺序调换一下
print(numbers)

nums = [5,1,3,2,4,9,7,0,8,6]
nums.sort()                 #排序
print(nums)


strings = ["yancy","yy","yuanyang","yelan"]
print(strings)
strings.reverse()
print(strings)
strings.sort()           #自动按照accsis编码排序,特殊字符会优先排序,注意:字符串不能和数字一起排序，会报错
print(strings)

numbers.extend(strings)  #扩展列表。可以将其他的列表追加到该列表来.这个表示把string列表增加到numbers列中来
print(numbers)


str1 = ["aa","bb","yy","cc",["yuanyang","yelan"]]
str2 = str1.copy()      #浅拷贝,只拷贝第一层的（即第一层的变量不包括子列表会被独立的开辟一块内存地址），如果列表里面镶嵌了子列表，那么第二层的列表里面的所有数值都会当成一个内存地址（即2个列表共用的同一个内存地址，都把内存指针指向了这个内存地址）
print(str1)
print(str2)
str1[0] = "啊啊"          #修改第一个元素为汉字
str2[4][1] = "叶兰"       #修改第4个元素的第一个元素为汉字
print(str1)
print(str2)


import sys
import copy                 #导入模块，说道模块有个sys模块是c语音写的，所以我们在python的环境变量中是无法找到sys.py的模块的
address_1 = ["北京","上海","广东","湖北","湖南",["袁阳","叶兰"]]
address_2 = copy.deepcopy(address_1)     #导入copy模块，用这个模块的深度复制已达到完全的拷贝
print(address_1)
print(address_2)
address_1[0] = "beijing"
address_2[5][1] = "yy"
print(address_1)
print(address_2)

for i in address_1:
    print(i)

num = [1,2,3,4,5,6,7,8,9]
print(num[0:-1:2])          #打印从第一个元素到倒数第一个元素，即所有元素，并空一格打印一个
print(num[::2])             #打印所有，并空一格打印一个
print(num[:])               #如果省略了数字就默认以0开头以-1结尾（即从头到尾的打印）
print(num[::])              #同上


person = ["name",["saving",10000]]
p1 = copy.copy(person)  #扩展中浅拷贝的方式
p2 = person[:]
p3 = list(person)
print(p1)
print(p2)
print(p3)

p1[0] = "yy"
p2[0] = "yancy"
p3[0] = "yuanyang"
print(p1)
print(p2)
print(p3)





