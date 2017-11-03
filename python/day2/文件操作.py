#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy

#-------------------------------------------------------------------------------------------------------------------
# data = open("filetest",encoding="utf-8").read()   #读取文件内容
# print(data)


#读  读模式默认不能写文件
f = open("filetest",'r',encoding="utf-8",)       #文件句柄
'''
-------------------------------------------------------------------------------------------------------------------
### r = read 读取
print(f.read())                 #将读取到内存中的文件打印出来
data = f.read()                 #将读取的文件内容赋值给变量
data2 = f.read()                #将读取的文件内容赋值给变量
print(data)
print('--------data2-------',data2)

print(f.readline())                 #readline()函数默认打印第一行
print(f.readlines())                   #readlines()函数把文件中的每一行做为一个元素输出到一个列表中
'''

'''
-------------------------------------------------------------------------------------------------------------------
print(f.tell())                 #打印tell,就是把当前光标在文件中的位置打印出来，0表示在最开头
print(f.readlines()); print(f.tell())   #当使用readlines把所有内容打印后，光标会到最后一个字符的的位置。

print(f.read());  print(f.tell())      #read函数默认也是打印所有内容的。
print(f.read(5));   print(f.tell())     #read(number)表示打印多个字符。
f.seek(10); print(f.tell())              #seek指定回到哪个位置，0表示开头。
'''

'''
-------------------------------------------------------------------------------------------------------------------
for i in range(5):                  #使用循环打印前5行
    print(f.readline())

for line in f.readlines():             #使用循环打印readlines列表中的所有元素就可以读取文件。是不是觉得这样多此一举？yes，是的，不过，这是为了下面做准备。
    print(line.strip())                 #strip可以去掉空行
'''


'''
-------------------------------------------------------------------------------------------------------------------
#打印前面10行
for index,line in enumerate(f.readlines()):   #使用enumerate函数结合index将索引和列表元素都取出来，并在下面判断当索引为9的时候，终止循环，这样就可以只打印前10行了。
#使用enumerate会把所有内容读取到内存中去，如果是很大的文件，这样子就GG了。
    if index == 10:
        print("--"*50)
        continue
    print(line.strip())
'''

'''
-------------------------------------------------------------------------------------------------------------------
#下面是用另一种方法打印前10行.
count = 0               #2、因为不能再打印下标了，所以要自己弄一个计数器，记录循环了多少行了。
for line in f:          #1、循环的时候每一次只加载一行到内存，循环下一行的时候，删除上一行。
    if count == 9:      #4、循环到到第10次的时候，打印一个分割线，并终止循环
        print("-"*50)
        count += 1      #3、每循环一行加1。
        continue
    print(line.strip()) #5、然后把剩下的所有内容都打印出来
    count +=1
'''


'''
-------------------------------------------------------------------------------------------------------------------
#写  写模式默认打开后不能读文件
f = open("filetest2",'w',encoding="utf-8",)    #注意了，w写模式会自己打开一个新文件，如果指定的文件名已经存在会把里面的内容清空，很危险啦，一不小心就删库到跑路了。
### w = write 写入
f.write("轻轻的我走了，正如我轻轻的来，\n")    #向文件中写入内容
f.write("我挥一挥衣裳袖子，不带走一只老母鸡。\n")
f.write("叶兰姐姐，我爱你！")

#使用append追加的好处和w的区别是：不会删除原来文件中的内容，只会在后面追加，相当于shell中">>" 和 ">"的区别
f = open("filetest2",'a',encoding="utf-8",)
### a = append 追加
f.write("\n怀念和你一起看星星的日子！")


f.truncate(5)                 #截断操作，从第一个光标开始截取指定长度的字符。只能在append模式下用。
'''

'''
-------------------------------------------------------------------------------------------------------------------
#文件修改1
###
# f = open("filetest",'r+',encoding="utf-8")   #文件句柄  r+表示读写 既能读也能写
# print(f.readline()); f.write("xx"*50)         #打印文件第一行的内容，并写入50个XX到文件中。注意：这个写入的内容会被追加到文件最后，没办法指定它的具体位置。

f = open("filetest",'w+',encoding="utf-8")   #文件句柄  w+表示写读
f.write("xx"*50);f.seek(0);print(f.readline())  #栗子:写入后再读取文件内容

f = open("filetest",'a+',encoding="utf-8")    #文件句柄  a+表示追加 读写
f.write("--"*50);f.seek(0);print(f.readline())  ##栗子:追加写入后读取文件内容

f = open("filetest",'rb')    #文件句柄   rb表示以二进制的格式读取文件
print(f.readline())           ##栗子:这时候读取文件会发现所有行的前面都有一个b，表示这是一个字节类型。

f = open("filetest",'wb')    #文件句柄   wb表示以二进制的格式写入文件
f.write("hello yelan jiejie!\n".encode())  #栗子:使用wb方式写入字符串默认会以utf的格式写入，这时会报错，需要用encode把字符串格式成btye格式
-------------------------------------------------------------------------------------------------------------------
'''

# #其他
# print(f.encoding)           #打印文件格式编码
# print(f.fileno())           #打印操作系统维护文件IO接口编号，基本上用不到这个。忘记它吧！
# print(f.name)               #打印这个文件的文件名
# print(f.isatty())           #查看这台设备是不是一个终端设备，比如打印机，返回bool值。这个一般在底层开发才用。基本上用不上，这个，忘记它吧！
# print(f.readable())         #判断文件是否可读，返回bool值
# print(f.writable())         #判断文件是否可写，返回bool值
# print(f.flush())            #强制刷新内存中的缓存内容写入到硬盘，要求内存每缓存一次数据都要写入硬盘后再返回写入完成。
#
# #flush的案例  yum安装进度条揭秘
# import sys,time             #导入sys标准库包和time包
# for i in range(50):
#     sys.stdout.write("#")   #使用标准输出打印"#"，可以把#号打印在一行，不换行。
#     sys.stdout.flush()      #使用flush强制刷新内存中的"#"写入到文件中，不然会出现内存把多个#号缓存在一起后一起打印出来。
#     time.sleep(0.01)        #每打印一个#号暂停0.01s
#
# f.close()                               #关闭文件，默认会自动关闭
with open("filetest","r",encoding="utf-8") as f:    #关闭文件的第二种方法，使用with。这样在打开文件操作完毕后会自动关闭文件，妈妈再也不用担心我忘记关闭文件了。
    print(f.readline())
    for line in f:
        print(line)

