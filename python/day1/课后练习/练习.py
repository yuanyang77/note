#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
username = "yy"
password = "linfan77"

count = 0
while count < 3:
    user = input("input you username: ")
    passwd = input("input you passwd")
    if user == username and passwd == password:
        print("welcome to login!")
        break
    elif password != passwd:
        print("you are password is not OK")
    else:
        print("checkou you username")
        count += 1
    if count == 3:
        temp = input("are you is want to doing? Y/N?")
        if temp != "n":
            count = 0
else:
    print("welocome to doing!")





