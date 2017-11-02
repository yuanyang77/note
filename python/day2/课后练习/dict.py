# #！/usr/bin/env python
# # -*- coding: utf-8 -*-
# # Author:yancy
#
# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
#
# av_catalog["大陆"]["1024"][1] = "用VPN吧，骚年！"
#
# av_catalog.setdefault("大陆",{"www.baidu.com":[1,2]})
# # print(av_catalog)
#
# info = {
#     "stu1101":"TenLan Wu",
#     'stu1102':"LongZe Luola",
#     'stu1103':"XiaoZe Maliya",
# }
#
# b = {
#     'stu1101':"Alex",
#     1:3,
#     2:5
# }
#
# info.update(b)
# print(b)
#
#
# info = {
#     'stu1101': "TengLan Wu",
#     'stu1102': "LongZe Luola",
#     'stu1103': "XiaoZe Maliya",
# }
#
# for i in info:
#     # print(i,info[i])
#     pass
# for k,v in info.items():
#     print(k,v)
#
# kik = {}
# print(kik)
# kik['name'] = "yancy"
# print(kik)
# kik ['name'] = "yuanyang"
# print(kik)
# # del kik["name"]
# # print(kik)
#
# kik.clear()
# print(kik)
# del kik
# # print(kik)
#
# yy = {'names':'yy','["age",18]':'["age",25]'}
# print(yy)
#

data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}

exit_flag = False

while not exit_flag:
    for i in data:
        print(i)
    choice = input("选择进入1>>:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("选择进入2>>:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入3>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t",i4)
                        choice4 = input("最后一层，按b返回>>:")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True