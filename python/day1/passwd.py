# -*- coding: utf-8 -*-
# Author:yancy
import getpass

username = input("username: ")
#password = getpass.getpass("password: ")
password = input("username: ")

_username = "yy"
_password = "linfan77"

if _username == username and _password == password:
    print ("Welcome usuer {name} login...".format(name=username))
else:
    print("Invalid username or password!")


#print(username,password)
