#-*-coding:utf-8-*-
# __author__ = 'yancy'
#
import sys
print(sys.getdefaultencoding())


msg = "你好"

msg_gb2312 = msg.decode("utf-8").encode("gb2312")           #UTF-8转换成GB2312，
gb2312_to_gbk = msg_gb2312.decode("gbk").encode("gbk")      #GBK转GBK，好像没啥要转的

print(msg)
print(msg_gb2312)
print(gb2312_to_gbk)

---------------------------------------------------------------------
#-*-coding:gb2312 -*-   #这个也可以去掉
__author__ = 'yancy'

import sys
print(sys.getdefaultencoding())


msg = "你是我最爱的人"
#msg_gb2312 = msg.decode("utf-8").encode("gb2312")
msg_gb2312 = msg.encode("gb2312") #默认就是unicode,不用再decode,喜大普奔
gb2312_to_unicode = msg_gb2312.decode("gb2312")     #gb2312转gb2312,多此一举，MDZZ
gb2312_to_utf8 = msg_gb2312.decode("gb2312").encode("utf-8")    #gb2312转utf8，先解码，告诉系统我当前是gb2312,再编码成utf8

print(msg)
print(msg_gb2312)
print(gb2312_to_unicode)
print(gb2312_to_utf8)