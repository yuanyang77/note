# -*- coding: utf-8 -*-
# Author:yancy

age_of_yy = 25
count = 0
while True:
    if count == 3:
        break
    guess_age = int(input("guess age: "))
    if guess_age == age_of_yy:
        print("yes,you got it.")
        break
    elif guess_age > age_of_yy:
        print("think smaller...")
    else:
        print("think bigger!")

    count += 1
