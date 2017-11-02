names = ("yy","yuanyang","linfan","yancy") #定义一个元组，元组支持的方法列表都支持而且元组仅仅支持两种方法
print(names)
print(names.count("yancy"))     ##统计字符串在该列表出现的次数,注意：不能把元素中的单个字母拿出来找，要找的字符串必须存在于元素中。
print(names.index("yancy"))     #超照列表中的某个值所对应的索引ID，这个ID会和第一项匹配，如果出现了就直接匹配出来不会继续往下查找了