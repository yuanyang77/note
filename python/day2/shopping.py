#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:yancy

product_list = [
    ('Iphone',6000),
    ('Mac Pro',13000),
    ('BiKe',3000),
    ('Watch',10000),
    ('Coffee',31),
    ('Book',50),
]
shop_list = []
salary = input("input you salary: ")

if salary.isdigit():
    salary = int(salary)
    while True:
        # for item in product_list:
        for index,item in enumerate(product_list):    #enumerate 会把列表的index和内容都打印出来
            # print(product_list.index(item),item)
            print(index,item)

        user_choice = input("请选择要购买的商品>>>: ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_itme = product_list[user_choice]
                if p_itme[1] <= salary:
                    shop_list.append(p_itme)
                    salary -= p_itme[1]
                    print("Added %s into shopping cart.your current balance is \033[32;1m%s\033[0m" %(p_itme,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]\033[0m" %(salary))
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == "q":
            print("---------shopping list ----------")
            for p in shop_list:
                print (p)
            print("\033[32;1m你的余额还有：\033[0m" ,(salary))
            exit()
        else:
            print("ivnalid option")
