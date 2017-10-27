#! coding: utf-8
# 判断输入的年龄对不对
age_of_yy = 25
guess_age = int(input("guess age:"))
if guess_age == age_of_yy :
    print("yes,you got it.")
elif guess_age > age_of_yy:
    print("think smaller...")
else:
    print("think bigger!")
