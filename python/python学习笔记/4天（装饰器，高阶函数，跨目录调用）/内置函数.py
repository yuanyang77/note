#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy

# abs()
# 取绝对值,不管是负数还是正数都得出正数
print(abs(-7))

# all()
# 列表中有 0 就非真，没有0就是真。负数也是真。
print(all([0,-5,3]))
#返回flase
print(all([-1,5,3]))
#返回true

# any()
# 列表中只要有一个是真，返回就为真。
print(any([]))
#返回flase,因为是空，没有一个为真
print(any([-1,0,1]))
#返回true

# ascii()
# 把内存中的数据变成一个可打印的字符串，没什么卵用，忘记它吧。

# bin()
# 10进制转2进制
print(bin(255))
#返回  0b11111111

# oct()
# 把10进制转换成8进制     r
print(oct(8))
# 返回0o10

# hex()
# 把10进制转换成16进制
print(hex(10))
# 返回0xa

# bool()
# 判断真假，     空字典，空字符串，都为假
print(bool([0]))

# bytes()
#将一个字符串转换成字节类型
print(bytes('中国','utf-8'))
#返回     b'\xe4\xb8\xad\xe5\x9b\xbd'

# str
# 将字符类型/数值类型等转换为字符串类型
print(str(123))
#返回 '123'



# bytearray()
# 根据传入的参数创建一个新的字节数组
print(bytearray('中国','utf-8'))
# 返回bytearray(b'\xe4\xb8\xad\xe5\x9b\xbd')

# callable()
#检测对象是否可被调用，可以返回True,不可以返回false
listr = [1,2]
print(callable(listr))
#返回 False   列表不能被调用
def test():pass
print(callable(test))
#返回True


# chr()
#返回整数所对应的Unicode字符
print(chr(100))
# 返回 d

# ord()
#返回Unicode字符对应的整数,正好和上面的chr反过来
print(ord('d'))
# 返回100R

# classmethod()
# 标示方法为类方法的装饰器

class Province:
    country = "中国"
      
    def __init__(self, name):
        self.name = name

    @classmethod
    def show(cls):  # 类方法，由类调用，最少要有一个参数cls，调用的时候这个参数不用传值，自动将类名赋值给cls
        print(cls)

# 调用方法
Province.show()

# compile()
# 将字符串编译为代码或者AST对象，使之能够通过exec语句来执行或者eval进行求值
code1 = 'for i in range(0,10): print (i)'
compile1 = compile(code1,'这里是内容描述','exec')
exec (compile1)

# compilex
# 创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数是字符串，则不需要指定第二个参数。
# 参数real：int，long，float或字符串。
# 参数imag：int，long，float。

# delattr()

# dict
#创建数据字典
yy = dict()
print(yy)
# 返回 ｛｝空字典
yy2 = dict(name = yy,age = 25)
print(yy2)


# dir()
#返回对象或者当前作用域内的属性列表
a = {}
print(dir(a))

# divmod()
#返回两个数值的商和余数
print(divmod(5,2))
print(divmod(3.7,1.2))


# eval()
#将字符串str当成有效的表达式来求值并返回计算结果
print(eval('1+2+3+4+5'))
#返回15

# exec
#执行字符串或complie方法编译过的字符串，没有返回值
exec ('a=3+5')
print(a)

# filter()
#使用指定方法过滤可迭代对象的元素,过滤出自己想要的
#过滤器，构造一个序列，等价于[ item for item in iterables if function(item)]，在函数中设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据。
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)

# float
# 将一个字符串或整数转换为浮点数
print(float())
# 返回 0.0
print(float(3))
# 返回 3.0

# format()
#格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法
print("my name is {0}".format("yancy"))
# 返回 my name is yancy


# frozenset()　　
# 创建一个不可修改的集合。
# print(frozenset([iterable]))
# set和frozenset最本质的区别是前者是可变的，后者是不可变的。当集合对象会被改变时（例如删除，添加元素），只能使用set，
# 一般来说使用fronzet的地方都可以使用set。
# 参数iterable：可迭代对象。

# getattr()
#获取对象的属性
# print(object, name [,defalut])
print(getattr(list, 'append'))


# globals()
#返回当前程序中所有的全局变量
print(globals())

#hasttr
# 判断对象object是否包含名为name的特性
# hasattr(object，name)

print(hasattr(list,'append'))
# 返回True

# hash()
# 哈希值
# 如果对象object为哈希表类型，返回对象object的哈希值。哈希值为整数，在字典查找中，哈希值用于快递比价字典的键。
# 两个数值如果相等，则哈希值也相等。

# help()

# hex()

# locals()
#打印函数中所有的居部变量
def test2():
    locals_var = 3
    print(locals())
test2()

# max()
#返回列表最大值
print(max([1,5,2,3]))
# 返回 5

# min()
#返回列表最小值
print(min([1,5,2,3]))
# 返回 1

# next()
# 返回一个可迭代数据结构（如列表）中的下一项

# map()
# map(function, iterable,...)
# 对于参数iterable中的每个元素都应用fuction函数，并将结果作为列表返回。
# 如果有多个iterable参数，那么fuction函数必须接收多个参数，这些iterable中相同索引处的元素将并行的作为function函数的参数。
# 如果一个iterable中元素的个数比其他少，那么将用None来扩展改iterable使元素个数一致。
# 如果有多个iterable且function为None，map()将返回由元组组成的列表，每个元组包含所有iterable中对应索引处值。
# 参数iterable必须是一个序列或任何可遍历对象，函数返回的往往是一个列表(list)。
#
li = [1,2,3]
data = map(lambda x :x*100,li)
print(type(data))
data = list(data)
print(data)
#
# 运行结果：
#
# <class 'map'>
# [100, 200, 300]

# id()
# 返回对象的内存地址
a = 11
print(id(a))

# input()
# 获取用户输入内容
name = input("you name is : ")


# int()
# 将一个字符串或数值转换为一个普通整数
print(int('123'))
# 返回 123

# isinstance()
# 检查对象是否是类的对象，返回True或False
# isinstance(obj, cls)
class foo(object):
    pass
obj = foo()
isinstance(obj,foo)

# issubclass()　　检查一个类是否是另一个类的子类。返回True或False
# issubclass(sub, super)
# 检查sub类是否是super类的派生类（子类）。返回True 或 False
class Foo(object):
    pass

class Bar(Foo):
    pass

issubclass(Bar, Foo)

# iter()
               # iter(o[, sentinel])
# 返回一个iterator对象。该函数对于第一个参数的解析依赖于第二个参数。
# 如果没有提供第二个参数，参数o必须是一个集合对象，支持遍历功能（__iter__()方法）或支持序列功能（__getitem__()方法），
# 参数为整数，从零开始。如果不支持这两种功能，将处罚TypeError异常。
# 如果提供了第二个参数，参数o必须是一个可调用对象。在这种情况下创建一个iterator对象，每次调用iterator的next()方法来无
# 参数的调用o，如果返回值等于参数sentinel，触发StopIteration异常，否则将返回该值。

# len()  获取对象的长度，对象可以是列表，元组，字符串，字典
print(len([1,2,3,4,5,]))
# 返回  5

# list
# 列表构造函数
list([iterable])
# 参数iterable是可选的，它可以是序列，支持编译的容器对象，或iterator对象。

# object
# 获取一个新的，无特性(geatureless)对象。Object是所有类的基类。它提供的方法将在所有的类型实例中共享。
# 该函数时2.2.版本新增，2.3版本之后，该函数不接受任何参数。

# open()
# 打开文件
f = open('test.txt','w',encoding="utf-8")
f.write('123455')

# pow()
#求幂函数
r = pow(2, 10)  # 2的10次方
print(r)

# print()
# 输出函数


range()
# 根据需要生成一个指定范围的数字，可以提供你需要的控制来迭代指定的次数
for i in range(10,20):
    print(i)

# repr()　　将任意值转换为字符串，供计时器读取的形式
print(repr(123456))

# reversed()
# 反转，逆序对象
# 返回一个逆序的iterator对象。参数seq必须是一个包含__reversed__()方法的对象或支持序列操作(__len__()和__getitem__())
# 该函数是2.4中新增的

round()
# 四舍五入
print(round(0.05))
# 返回 0
print(round(1.8))
# 返回 2

# set
#  返回一个新的set对象，可以选择从iterable取得的元素，set是一个内置的类,一般为集合对象

# setattr()　　与getattr()相对应，setattr(object,name,value) 参数是一个对象，一个字符串和一个任意值。字符串可以命名现有属性或新属性。如果对象允许，该函数将赋值给该属性。

# slice
# 切片功能,  slice(start, stop[, step])
# print(slice(3,5[1,2,3,4,5,6,7,8,9]))

# sorted()
#排序
print(sorted([36,6,-12,9,-22]))
print(sorted([36,6,-12,9,-22],key=abs) )
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# >>> sorted([36,6,-12,9,-22])  列表排序
# [-22, -12, 6, 9, 36]
# >>> sorted([36,6,-12,9,-22],key=abs) 高阶函数，以绝对值大小排序
# [6, 9, -12, -22, 36]
# >>> sorted(['bob', 'about', 'Zoo', 'Credit'])  字符串排序，按照ASCII的大小排序
# ['Credit', 'Zoo', 'about', 'bob']
# 如果需要排序的是一个元组，则需要使用参数key，也就是关键字。
# >>> a = [('b',2), ('a',1), ('c',0)]
# >>> list(sorted(a,key=lambda x:x[1]))   按照元组第二个元素排序
# [('c', 0), ('a', 1), ('b', 2)]
# >>> list(sorted(a,key=lambda x:x[0]))   按照元组第一个元素排序
# [('a', 1), ('b', 2), ('c', 0)]
# >>> sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower) 忽略大小写排序
# ['about', 'bob', 'Credit', 'Zoo']
# >>> sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True) 反向排序
# ['Zoo', 'Credit', 'bob', 'about']


 # staticmethod()  在类中定义一个静态方法的函数，通常@staticmethod 下面接一个函数，如此使用

 # str
 str('1,2,3')

 # sum()
print(sum([1,2,3],4))

 # super

 # tuple
print(tuple([1,2,3,4,5,]))
#把列表替换成元组
print(tuple("fjaljahg"))
#把字符串替换成元组

 # type
yy = 11
print(type(yy))
# 返回 <class 'int'>

# vars()
# vars([object])  使用__dict__属性返回模块，类，实例或任何其他对象的__dict__属性。

# zip()
list_1 = [1,2,3]
list_2 = ['a','b','c']
s = zip(list_1,list_2)
print(list(s))

# 运行结果：
# [(1, 'a'), (2, 'b'), (3, 'c')]