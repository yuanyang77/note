#coding=utf-8
#定义数组范围
arr = range(10)

#取出从第一个到第三个索引的元素，包含起始位置，不包含结束位置。
print arr[1:3]

#取出从指定元素到最后一个元素
print arr[3:]

#取出所有元素
print arr[:]

#取出所有元素，从最后一个往前排列。
print arr[::-1]

#切片模拟添加元素
arr[1:1] = [6]  #在第一个元素后面添加了一个元素6
print arr

#切片模拟删除
arr[2:5]=[]     #删除了索引为2 3 4的元素
print arr

#删除某个指定的元素
del arr[0]
print arr

arr = [1,2,'a',3]
arr.reverse()      #倒置排序
arr.remove('a')    #删除指定值的元素
print arr
