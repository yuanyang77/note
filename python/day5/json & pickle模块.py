# 用于序列化的两个模块
#
# json，用于字符串 和 python数据类型间进行转换
# pickle，用于python特有的类型 和 python的数据类型间进行转换
# 补充说明：将数据通过特殊的形式转换成只有python解释器识别的字符串，这个过程我们叫做序列化，而把哪些python能够识别的字符串转换成我们能看懂的叫做反序列化。
# Json模块提供了四个功能：dumps、dump、loads、load
#
# pickle模块提供了四个功能：dumps、dump、loads、load

#1.将数据通过特殊的形式转换为只有python语言知识的字符串并写入文件

import pickle,json
# pickle
#     1.>用于python特有的类型 和 python的数据类型间进行转换
#     2.>pickle模块提供了四个功能：dumps、dump、loads、load.
#     补充说明：将数据通过特殊的形式转换成只有python解释器识别的字符串，这个过程我们叫做序列化，而把哪些python能够识别的字符串转换成我们能看懂的叫做反序列化。
data = {"k1":123,"k2":'hello'}
p_str = pickle.dumps(data)
print(p_str)
f = open("test.txt","wb")
f.write(p_str)

#2.上面的写入文件的方法也可以这么玩,看起来更简单
with open("test.txt",'wb') as f:
    pickle.dump(p_str,f)


# 把存入文件的东西读出来
f = open("test.txt",'rb')
print(pickle.loads(f.read()))

f = open('test.txt','rb')
print(pickle.load(f))

# json
# 用于序列化的两个模块
#     1>.json:用于字符串 和 python数据类型间进行转换
#     2>.pickle:用于python特有的类型和python的数据类型间进行转换
#     json模块提供了四个功能：dumps、dump、loads、load
#     pickle模块提供了四个功能：dumps、dump、loads、load

#json.dump 把数据通过特殊形式转换为所有程序语言都认识的字符串，并写入文件
data = {"k1":123,"k2":'hello'}
j_str = json.dumps(data)
print(j_str)

with open("test2.txt",'w') as fp:
    json.dump(data,fp)


# 存数据方式一：
accounts = {'id':7,'name':'yy','age':25}
f = open("test2.txt","w")
json_str = json.dumps(accounts)
f.write(json_str)
# 存数据方式二：
with open("test2.txt","w") as fp:
     json.dump(accounts,fp)
# 读取数据的方法一：
f = open("test2.txt","r")
print(json.loads(f.read()))
# 方法二:
f = open("test2.txt","r")
print(json.load(f))