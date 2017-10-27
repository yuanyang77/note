#!/usr/bin/env python
#! -*- coding: utf-8 -*-

#实例1
#arr = ['user:pwd','user1:pwd1',"user2:123"]
#user = 'user1'
#pwd = 'pwd1'
#
#user_pwd = user+':'+pwd
#
#if user_pwd in arr:
#    print 'success'
#else:
#    print 'fail'

#===============================================================

#实例2
#arr = ['user:pwd','user1:pwd1',"user2:123"]
#user = 'user'
#pwd = 'pwd'

#user_list = []
#pwd_list = []
#for i in arr:
#    temp = i.split(':')
#    user_list.append(temp[0])
#    pwd_list.append(temp[1])
#if user in user_list:
#    if pwd == pwd_list[user_list.index(user)]:
#        print 'success'
#    else:
#        print "wrong password"
#else:
#    print 'user no exists'
#==================================================================


#实例2
arr = ['user:pwd','user1:pwd1',"user2:123"]
user = 'user1'
pwd = 'pwd'

user_exists = False

for u in arr:
    temp = u.split(':')
    if temp[0]==user:
        if temp[1]==pwd:
            msg = 'success'
        else:
            msg = 'wrong pwd'
        user_exists=True
        print msg
        break
if not user_exists:
    print 'msg'
