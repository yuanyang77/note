#-*- coding: utf-8 -*-
#split把字符串切割为list 
print 'hello,yy,world'.split(',')

#join把list拼接成字符串
print ','.join(['hello','yy','world'])

#replace
print 'hello,world'.replace(',','|')


#实例
my_str = 'hello,reboot:you,xxx,xxx:xxx'
print my_str.replace(',',':').split(':')
