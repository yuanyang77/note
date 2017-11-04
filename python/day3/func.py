#!/usr/bin/env python
# #!--*-- coding: utf-8 --*--
# # Author yancy
import time

#定义一个有返回值的函数，这个函数被调用后会返回7
def fun():
    "the test 1"
    print("in the func test1")
    return 7

#定义一个过程，过程就是没有返回值的函数，
# 注：没有定义返回值，默认会返回None
def fun2():
    "the test 2"
    print("in the func test2")

#把上面定义的函数赋值给变量，这种方式也可以把函数的返回值打印出来.打印函数返回值，可以调用赋值了函数的变量，也可以直接调用函数本身。以下方法都可以调用函数。
x = fun()
y = fun2()
print("for fun return is %s" % x)
print("for fun return is %s" % y)
print("for fun return is %s" % fun())
print("for fun return is %s" % fun2())
fun()
fun2()

# 栗子：
def loger():
    time_format = "%Y-%m-%d %X"                         #定义时间格式，%X表示打印小时分钟秒
    time_current = time.strftime(time_format)           #利用time模块的strftime，将日期按照之前定义好的time_format形式打印出来！
    with open("log.txt","a+") as f:                     #打开log.txt文件，写入内容
        f.write("%s end action\n" %time_current)
loger()

#----------------------------------------------------------------------------------

#函数的参数和调用
#函数名后面括号里面的参数叫做形式参数，等着实际参数传递值给它，简称形参。如果没有传递，将返回默认值

#函数参数的第一种调用方法：单独使用位置参数或者关键字参数
def fun3(x,y):
    print(x)
    print(y)
    return

#在函数调用过程中传递给函数的参数叫实际参数，简称实参
fun3(1,2)               #在函数调用赋值过程中,按照和形参顺序一一对应来给形参传参的写法叫位置参数。
fun3(y=20,x=10)         #在函数调用赋值过程中,使用函数中的形参关键字来给形参传递在值的写法，叫关键字参数，关键字参数的书写顺序可以和形参的顺序不一样。

#函数参数的第二种调用方法：混合使用位置参数和关键字参数
#位置参数和关键字调用可以这样用，但是要注意！位置参数要放在关键字参数的前面！换句话说就是关键字参数要放在位置参数的后面，然后后面的所有关键字参数可以无序的传参数
def fun4(x,y,z):
    print(x)
    print(y)
    print(z)
fun4(199,z=299,y=399)

#默认参数
#用途：1.定义程序的安装路径；2.定义数据库连接时的端口等等
#我们可以定义一个默认参数，调用这个函数的时候，默认参数并非必须传递，如果传递参数就会打印传递的参数，如果不传递参数就打印默认的参数；
def fun5(x,y=2):
    print(x)
    print(y)
fun5(7,700)
fun5(7)
fun5(y=10,x=20)

#参数组
#我们在传参的时候多传递或者少传递参数都会导致程序脚本报错，但是有时候，我们可能事先并不知道需要传递多个多参数，因此我们就可以定义一个参数组，用于传递参数数量不固定的时候！
#若你的函数在定义时不确定用户想传入多少个参数，就可以使用非固定参数
#定义一个参数组，当调用该函数的时候传入的实际参数会自动将其变成一个tuple[接受N个位置参数，转换成元组的形式]
#*args
# *args 会把多传入的参数变成一个元组形式
def fun6(*args):
    print(args)
fun6(1,2,3,4,5,4,5,6,7,7)
fun6(*[100,200,300,400,500])
fun6()              #这个会返回一个 （）说明*args不传递值也是可以的

#**kwargs
# *kwargs 会把多传入的参数变成一个dict形式,#接受N个关键字参数，转换成字典的方式,传递的参数相当于key和value
def fun7(name,age,*args,**kwargs):
    print(name,age,args,kwargs)

fun7("yy","25")     #输出 yy 25 () {} 后面这个{}就是**kwargs,只是因为没传值,所以为空
#输出  yy 25 () {}
fun7("linfan",25,"ops","python","golang",sex="m",province="hubei")
#输出设备 linfan 25 ('ops', 'python', 'golang') {'province': 'hubei', 'sex': 'm'}

#全局变量和局部变量
name = "yy"

def change_name(name):
    print("name is:",name)
    name = "yancy"
    print("name is",name)
change_name(name)
print("看看现在的name是什么？",name)

#输出如下：              从输出可以看到，函数体中定义的的局部变量，在函数运行完成后就失效了。
# name is: yy
# name is yancy
# 看看现在的name是什么？ yy

#递归函数：在函数内部，可以调用其他函数，如果一个函数在内部调自身本身，这个函数就是递归函数。
def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(int(n/2))
calc(10)
# 输出：
# 10
# 5
# 2
# 1

#打印从0到100
def add(n):
    print(n)
    n += 1
    if n <=100:
        return add(n)
add(0)


#高阶函数
def add(x,y,f):
    return f(x) + f(y)
res = add(3,-6,abs)
print(res)
