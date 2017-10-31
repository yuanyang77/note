# -*- coding: utf-8 -*-
# Author:yancy


age_of_yy = 25
for i in range(3):
    guess_age = int(input("guess age: "))
    if guess_age == age_of_yy:
        print("yes,you got it.")
        break
    elif guess_age > age_of_yy:
        print("think smaller...")
    else:
        print("think bigger!")
else:
    print("you have trice too many times... godeby!!")
