#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:yancy
product_list = [('Iphone',6000),
                ('MAC Pro',13000),
                ('Bike',1000),
                ('cffee',31),
                ('Book',80),
                ('watch',1500),
                ('wine',70)
                ]

salary = input("input you salary: ")
shop_list = []

if salary.isdigit():
    salary = int(salary)
    while True :
        for index,item in enumerate(product_list):
            print(index,item)

        user_choice = input("请选择要购买的商品>>>: ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_itme = product_list[user_choice]
                if p_itme[1] <= salary:
                    shop_list.append(p_itme)
                    salary -= p_itme[1]
                    print("Added %s into shopping cart.your current balance is \033[32;1m%s\033[0m " %(p_itme,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]\033[0m" %(salary))
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == "q":
            print("---------shoping list -----------")
            for p in shop_list:
                print(p)
            print("\033[32;1m你的余额还有：\033[0m",(salary))
            exit()
        else:
            print("ivnalid option")
