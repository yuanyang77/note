#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:yancy

msg = "我是中国人"
print (msg.encode("utf-8"))        #字符串转换成二进制
print (msg.encode(encoding="utf-8").decode("utf-8"))   #二进制转字符串