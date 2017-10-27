#coding:utf-8
unsort_list = [1,3,2,20,84,1000,933,12345,65535,11,222,65535]
max_num = 0
sec_num = 0
for i in unsort_list:
    if i > max_num:
        sec_num = max_num
        max_num = i
    elif i > sec_num:
        sec_num = i
print "最大的两个值为：%s,%s" %(sec_num,max_num)
