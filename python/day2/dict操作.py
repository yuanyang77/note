# 定义一个字典
info = {'name':'yy',
        'heigh':'175',
        'sex':'man',
        'hobby':'bike'
        }

#查  字典是无序的，所以不能用index来查
print(info.values())    #打印该字典的所有的value的值
print(info.keys())      #打印该字典的所有的keys值
print(info)             #打印字典中的所有内容
print(info.get('name')) #查找key名称是name所对应的value,如果有就返回其所对应的value,如果没有的话就不输出
print("address" in info) # 判断info这个字典中是否有adress这个key,如果没有就返回False，如果有就返回Ture，在python2.7中还可以这么写：info.has_key("adress")

print(info.setdefault("name2","yancy")) #该方法可以去取该字典是否存name这个值，如果存在就会返回后面定义的值，如果不存在就回新建一个key值对
print(info)

info.setdefault("place","湖北")       #该方法可以去字典去取相应的Key（place）值，如果没有取到(就说明没有定义这个key)，也就是新建一个新的key值
print(info)

#改
info['name'] = "袁阳"     #修改一个字典中的一个key所对应的value值
print(info)
info['age'] = '25'      #如果该字典没有对应的key，就是新增了一个key信息
print(info)


#删
del info["name"]        # 删除该字典中的name这个key
print(info)
info.pop("sex")         #删除该字典中的heigh
print(info)
info.popitem()          #随机删除该字典的一个Key信息
print(info)


#其他
a = {
'hobby':'bike',
'name' : 'yancy',
'age':'25'
}
b = {
'hobby':'ping-pong',
1:100,
2:200
}

a.update(b)         ##该方法可以将另外一个字典中的key和value更新到这个字典中，如果出现想用的key的话会用后面的字典中的value进行现有的value.
print(a)

c = dict.fromkeys([1,2,2,3,3,4,4],[444,{"name":"yancy"},555])   #这里面有2个列表，会自动将前面的列表去重并将去重后的每一个元素生成一个字典中所对应的key.然后将后面的列表当成一个内存地址同时赋值给没有key的元素
print(c)

c[3][1]["name"] = "叶兰"  #如果通过fromkeys定义生成的字典，修改其中任意一个key的值，那么所有的key的value都会跟着变化的.
print(c)

# for i in info:          #循环打印字典中的没有个key和value
#     print(i,info[i])

for k,v in info.items():    #这个循环会将字典先转换成一个列表，然后再打印出来，如果数据量较小的话和上面的循环的方法差不多，数据量大的时候不要使用
    print(k,v)
