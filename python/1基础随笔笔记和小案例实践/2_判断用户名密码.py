#! coding: utf-8
#! 判断输入的用户名和密码是否正确
import getpass
_username = 'yy'
_password = 'abc123'
username = raw_input("username:")

password = raw_input("password:")
if _username == username and _password == password:
    print("Welcome user {name} login..".format(name=username))
else:
    print ("Invalid username or password!")
