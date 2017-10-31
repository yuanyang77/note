hello world
	print ("hello world!")
	print ("你好，世界！")

变量
	name = "yy"					#把字符串赋值给变量的时候要用""
	age = 25					
	a = b = c = 10				#多个变量赋同一个值
	a, b, c = 1, 2, 3			#多个变量同时赋值
	print name
	print age

用户输入
	name = input("name: ")
	name = raw_input("name: ")   #python2中要使用raw_input
	age = int(input("age: "))    #input默认把所有输入都当成字符串，如果想要输入的数据是数字的话，需要加int强制把字符串转成数字类型。

	import getpass
	pwd = getpass.getpass("pwd: ") #输入密码如果要密文的话，需要用到getpass,getpass需要用import导入。

数据类型
	数字    number
		正数，负数，整数，小数都是数字类型
	整型    int 
		32int -2**31~2**31-1
		64int -2**63~2*63-1

	长整型

	浮点型  float	

	字符串  str
		字符串一般都要用单引号'',或者双引号"",或者三引号""" """  ''' '''(可以是三个双引号，也可以是三个单引号)

	列表    list
		在python中用[]表示

	字典    dict
		在python中用{}表示

	元组    tuple
		在python中用()表示

	日期    date

	布尔    bool
		真或假  True False  0 1

运算和运算符
	算术运算符
		+	加 - 两个对象相加	a + b 输出结果 30
		-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
		*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
		/	除 - x除以y	b / a 输出结果 2
		%	取模 - 返回除法的余数	b % a 输出结果 0
		**	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
		//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
        实例:
			#!/usr/bin/python3
			a = 21
			b = 10
			c = 0
			 
			c = a + b
			print ("1 - c 的值为：", c)
			 
			c = a - b
			print ("2 - c 的值为：", c)
			 
			c = a * b
			print ("3 - c 的值为：", c)
			 
			c = a / b
			print ("4 - c 的值为：", c)
			 
			c = a % b
			print ("5 - c 的值为：", c)
			 
			# 修改变量 a 、b 、c
			a = 2
			b = 3
			c = a**b 
			print ("6 - c 的值为：", c)
			 
			a = 10
			b = 5
			c = a//b 
			print ("7 - c 的值为：", c)
			以上实例输出结果：
			1 - c 的值为： 31
			2 - c 的值为： 11
			3 - c 的值为： 210
			4 - c 的值为： 2.1
			5 - c 的值为： 1
			6 - c 的值为： 8
			7 - c 的值为： 2


	比较（关系）运算符
		==	等于 - 比较对象是否相等	(a == b) 返回 False。
		!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
		<>	不等于 - 比较两个对象是否不相等	(a <> b) 返回 true。这个运算符类似 != 。
		>	大于 - 返回x是否大于y	(a > b) 返回 False。
		<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 true。
		>=	大于等于	- 返回x是否大于等于y。	(a >= b) 返回 False。
		<=	小于等于 -	返回x是否小于等于y。	(a <= b) 返回 true。
		实例：
			#!/usr/bin/python3
			a = 21
			b = 10
			c = 0
			 
			if ( a == b ):
			   print ("1 - a 等于 b")
			else:
			   print ("1 - a 不等于 b")
			 
			if ( a != b ):
			   print ("2 - a 不等于 b")
			else:
			   print ("2 - a 等于 b")
			 
			if ( a < b ):
			   print ("3 - a 小于 b")
			else:
			   print ("3 - a 大于等于 b")
			 
			if ( a > b ):
			   print ("4 - a 大于 b")
			else:
			   print ("4 - a 小于等于 b")
			 
			# 修改变量 a 和 b 的值
			a = 5;
			b = 20;
			if ( a <= b ):
			   print ("5 - a 小于等于 b")
			else:
			   print ("5 - a 大于  b")
			 
			if ( b >= a ):
			   print ("6 - b 大于等于 a")
			else:
			   print ("6 - b 小于 a")
			以上实例输出结果：
			1 - a 不等于 b
			2 - a 不等于 b
			3 - a 大于等于 b
			4 - a 大于 b
			5 - a 小于等于 b
			6 - b 大于等于 a

	赋值运算符
		=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
		+=	加法赋值运算符	c += a 等效于 c = c + a
		-=	减法赋值运算符	c -= a 等效于 c = c - a
		*=	乘法赋值运算符	c *= a 等效于 c = c * a
		/=	除法赋值运算符	c /= a 等效于 c = c / a
		%=	取模赋值运算符	c %= a 等效于 c = c % a
		**=	幂赋值运算符	c **= a 等效于 c = c ** a
		//=	取整除赋值运算符	c //= a 等效于 c = c // a
		实例：
			#!/usr/bin/python3
 			a = 21
			b = 10
			c = 0
			 
			c = a + b
			print ("1 - c 的值为：", c)
			 
			c += a
			print ("2 - c 的值为：", c)
			 
			c *= a
			print ("3 - c 的值为：", c)
			 
			c /= a 
			print ("4 - c 的值为：", c)
			 
			c = 2
			c %= a
			print ("5 - c 的值为：", c)
			 
			c **= a
			print ("6 - c 的值为：", c)
			 
			c //= a
			print ("7 - c 的值为：", c)
			以上实例输出结果：
			1 - c 的值为： 31
			2 - c 的值为： 52
			3 - c 的值为： 1092
			4 - c 的值为： 52.0
			5 - c 的值为： 2
			6 - c 的值为： 2097152
			7 - c 的值为： 99864

	逻辑运算符
		and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
		or	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
		not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
		实例：
			#!/usr/bin/python3
 			a = 10
			b = 20
			 
			if ( a and b ):
			   print ("1 - 变量 a 和 b 都为 true")
			else:
			   print ("1 - 变量 a 和 b 有一个不为 true")
			 
			if ( a or b ):
			   print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
			else:
			   print ("2 - 变量 a 和 b 都不为 true")
			 
			# 修改变量 a 的值
			a = 0
			if ( a and b ):
			   print ("3 - 变量 a 和 b 都为 true")
			else:
			   print ("3 - 变量 a 和 b 有一个不为 true")
			 
			if ( a or b ):
			   print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
			else:
			   print ("4 - 变量 a 和 b 都不为 true")
			 
			if not( a and b ):
			   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
			else:
			   print ("5 - 变量 a 和 b 都为 true")
			以上实例输出结果：
			1 - 变量 a 和 b 都为 true
			2 - 变量 a 和 b 都为 true，或其中一个变量为 true
			3 - 变量 a 和 b 有一个不为 true
			4 - 变量 a 和 b 都为 true，或其中一个变量为 true
			5 - 变量 a 和 b 都为 false，或其中一个变量为 false

	位运算符
		&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
		|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
		^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
		~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。
		<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
		>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
		实例：
			a = 0011 1100

			b = 0000 1101

			-----------------

			a&b = 0000 1100

			a|b = 0011 1101

			a^b = 0011 0001

			~a  = 1100 0011

	成员运算符
		in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
		not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
		实例：
			#!/usr/bin/python3
 			a = 10
			b = 20
			list = [1, 2, 3, 4, 5 ];
			 
			if ( a in list ):
			   print ("1 - 变量 a 在给定的列表中 list 中")
			else:
			   print ("1 - 变量 a 不在给定的列表中 list 中")
			 
			if ( b not in list ):
			   print ("2 - 变量 b 不在给定的列表中 list 中")
			else:
			   print ("2 - 变量 b 在给定的列表中 list 中")
			 
			# 修改变量 a 的值
			a = 2
			if ( a in list ):
			   print ("3 - 变量 a 在给定的列表中 list 中")
			else:
			   print ("3 - 变量 a 不在给定的列表中 list 中")
			以上实例输出结果：
			1 - 变量 a 不在给定的列表中 list 中
			2 - 变量 b 不在给定的列表中 list 中
			3 - 变量 a 在给定的列表中 list 中

	身份运算符
		is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
		is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
		
		is 与 == 区别：
		is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
		实例：
			#!/usr/bin/python3
 			a = 20
			b = 20
			 
			if ( a is b ):
			   print ("1 - a 和 b 有相同的标识")
			else:
			   print ("1 - a 和 b 没有相同的标识")
			 
			if ( id(a) == id(b) ):
			   print ("2 - a 和 b 有相同的标识")
			else:
			   print ("2 - a 和 b 没有相同的标识")
			 
			# 修改变量 b 的值
			b = 30
			if ( a is b ):
			   print ("3 - a 和 b 有相同的标识")
			else:
			   print ("3 - a 和 b 没有相同的标识")
			 
			if ( a is not b ):
			   print ("4 - a 和 b 没有相同的标识")
			else:
			   print ("4 - a 和 b 有相同的标识")
			以上实例输出结果：
			1 - a 和 b 有相同的标识
			2 - a 和 b 有相同的标识
			3 - a 和 b 没有相同的标识
			4 - a 和 b 没有相同的标识

	运算符优先级
		**	指数 (最高优先级)
		~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
		* / % //	乘，除，取模和取整除
		+ -	加法减法
		>> <<	右移，左移运算符
		&	位 'AND'
		^ |	位运算符
		<= < > >=	比较运算符
		<> == !=	等于运算符
		= %= /= //= -= += *= **=	赋值运算符
		is is not	身份运算符
		in not in	成员运算符
		not or and	逻辑运算符
		实例：
			#!/usr/bin/python3
 			a = 20
			b = 10
			c = 15
			d = 5
			e = 0
			 
			e = (a + b) * c / d       #( 30 * 15 ) / 5
			print ("(a + b) * c / d 运算结果为：",  e)
			 
			e = ((a + b) * c) / d     # (30 * 15 ) / 5
			print ("((a + b) * c) / d 运算结果为：",  e)
			 
			e = (a + b) * (c / d);    # (30) * (15/5)
			print ("(a + b) * (c / d) 运算结果为：",  e)
			 
			e = a + (b * c) / d;      #  20 + (150/5)
			print ("a + (b * c) / d 运算结果为：",  e)
			以上实例输出结果：
			(a + b) * c / d 运算结果为： 90.0
			((a + b) * c) / d 运算结果为： 90.0
			(a + b) * (c / d) 运算结果为： 90.0
			a + (b * c) / d 运算结果为： 50.0

字符串
	字符串操作：
		name = "my name is yy"

		print(name.capitalize())  # 首字母大写

		print(name.count("e"))  # 统计"e"这个字母在name变量中的字符串出现的次数

		print(name.center(50, "="))  # 打印50个字符，如果name这个变量中的字符串总个数不足50个，少出来的位置用“=”来填补，将name这个变量居中。

		print(name.ljust(50, '*'))  # 打印50个字符，如果name这个变量中的字符串总个数不足50个，少出来的位置用“=”来填补，但是不是讲name这个字符串居中，而是打印整个字符串，不够50个字符串的用“*"号填补。

		print(name.rjust(50, '-'))  # 这个和上面的相反,将整个字符串的占位打在右边，左边不足50个字符的用"-"填补

		print(name.endswith("jie"))  # 判断一个变量是否以“jie”这个字符串结尾，如果是就返回Ture

		name = "my \tname is yy"

		print(name)

		print(name.expandtabs(tabsize=50))  # 自定义tab的间隔打小，该处是指定tab的间隔是50个空格。

		print('yy'.find("e"))  # 在name这个字符串中查找含有name字样的索引，从左往右开始查找，将查找的第一个返回出来，也就是最靠左边的那个

		print('yy'.rfind('e'))  # 从左往右开始查找，将查找到的最靠右的匹配结果的索引取出来

		print(name[name.find("name"):])  # 字符串和列表都有相同的功能，都可以支持切片，比如这个例子就是取“n”这个字符后面的所有字符

		info = "I LOVE PLAY {A} and I love play {B}"

		print(info)

		print(info.format(A="ping-pong", B="basketball"))  # 以定义一个变量的形式传递一个参数到info的字符串中

		print(info.format_map({'A': 'football', 'B': 'volleyball'}))  # 以字典的形式传递一个参数到info的字符串中

		print('adA21'.isalnum())  # 判断前面的字符串是否仅仅包含[a-z][A-Z][0-9]

		print('adA'.isalpha())  # 判断前面的字符串仅仅包含[a-z][A-Z]

		print('1A'.isdecimal())  # 判断前面的数字是否是十六进制的数字

		print('2B'.isdigit())  # 判断该字符串是否是一个整数

		print('yy_1'.isidentifier())  # 判断是不是一个合法的标识符

		print('yy'.islower())  # 判断前面的字符串是否都是小写

		print('yy'.isupper())  # 判断前面的字符串是否都是大写

		print('696'.isnumeric())  # 判断该变量是否是一个十进制的数字

		print(' '.isspace())  # 判断前面的字符串是否是一个空格

		print('My Name Is yy'.istitle())  # 判断这个字符串的每个字母是否大写

		print('yy'.isprintable())  # 判断前面的字符串是否支持打印功能，一般字符串都是可以打印的。在linux中一切都是文件，一些tty，drive等终端文件是不能打印的，就可以用这个来判断，用途比较少

		print('+'.join(['1', '2', '3']))  # 将一个列表的信息追加到前面的字符串中

		print('yy'.lower())  # 将大写变成小写

		print('yy'.upper())  # 将小写变成大写

		print('\n yy'.lstrip())  # 只去掉左边的换行符或者空格

		print(' linghunbaidu \n '.rstrip())  # 只去掉左边和右边的换行符或者空格

		print(' yy \n'.strip())  # 去掉字符串左右两边的空格和换行符

		print('-----')

		passwd = str.maketrans("abclefghijklmnopqrstuvwxyz",
		                       '1234567890!@#$%^&*()_+-={}')  # 将前面的字符串后后面的数字和特殊字符一样匹配，对应的数字会转换成相应的字符。

		print("yy".translate(passwd))  # 将上面自定义的参数，合这里面的字符想对应，如果穿进去的参数没有对应的字符就不匹配。这个跟Linux的密码加密有点类似哟。

		print('yy'.replace('e', 'E', 2))  # 将字符串中的某个字符换成另外的一个字母或者数字（字符），后面可以匹配相应的次数，依次从左往右开始匹配。

		print('yy zheng jie'.split())  # 将字符串按照空格分成一个列表

		print('1+2+3+4+5'.split('+'))  # 用“+”作为分隔符，将其变成一个列表，如果不指定的话是以默认以空格分隔符的，例子如上

		print('yy'.swapcase())  # 将字符串中的大小写互换

		print('yy zheng jie'.title())  # 将以空格为分隔符的所有的小写字母变大写

		print('yy'.zfill(50))  # 总共需要打印50个字符，如果字符串不够的话前面用0占位

	字符串查询：
		1.使用索引，索引是从0开始的。
		list1 = "asdfjklbnvmcxzyuanyang"
		print (list1[:])		#查询list1中的所有内容
		print (list1[::])		#查询list1中的所有内容
		print (list1[1:5])		#查询list1中从索引为1到索引为5的元素，但不包括索引5在内。包括起点，不包括终点。
		print (list1[0:])		#查询list1中从第0个索引到最后一个索引的元素，其实就是查所有的内容了。
		print (list1[:8])		#查询list1中从第8个索引到第0个索引的内容，不包括第8个索引。
		print (list1[-1])		#查询list1中从最后倒数第一个元素
		print (list1[0:10:2])	#查询list1中从第0个索引到第10个索引中间的元素，并且每隔两个取出一个。
		以上实例输出结果：
			yancy is good boy
			yancy is good boy
			yancy is good boy
			ancy
			yancy is good boy
			y
			yancy is
			ynyi


	字符串格式化：
	    %c	 格式化字符及其ASCII码
      	%s	 格式化字符串
      	%d	 格式化整数
      	%u	 格式化无符号整型
      	%o	 格式化无符号八进制数
      	%x	 格式化无符号十六进制数
      	%X	 格式化无符号十六进制数（大写）
      	%f	 格式化浮点数字，可指定小数点后的精度
      	%e	 用科学计数法格式化浮点数
      	%E	 作用同%e，用科学计数法格式化浮点数
      	%g	 %f和%e的简写
      	%G	 %f 和 %E 的简写
      	%p	 用十六进制数格式化变量的地址
      	实例1：
	      	print ("my name is %s,my age is %d" %('袁阳',25))
	      返回结果：
	      	my name is 袁阳,my age is 25
	    实例2：
		    # -*- coding: utf-8 -*-
			# Author:yancy
			name = input("name:")
			age = int(input("age: "))
			print(type(age) ,type( str(age) ))
			job = input("job:")
			salary = input("salary:")

			info = '''
			---------- info of %s ---------
			Name:%s
			Age:%s
			Job:%s
			Salary:%s
			'''%(name,name,age,job,salary)

			#print (info)

			info2 = """
			--------- info of {_name}
			Name:{_name}
			Age:{_age}
			Job:{_job}
			Salary:{_salary}
			""".format(_name=name,
			           _age=age,
			           _job=job,
			           _salary=salary)
			#print (info2)

			info3 = """
			----------- info of {0} ------------
			Name:{0}
			Age:{1}
			Job:{2}
			Salary:{3}
			""".format(name,age,job,salary)
			print (info3)

	字符串拼接：
		print("袁阳"*5)
		print("袁阳"+"叶兰"+"林姗")
		以上实例输出结果：
			袁阳袁阳袁阳袁阳袁阳
			袁阳叶兰林姗




列表
字典
元组
数组
切片

条件语句
	if  表达式 ：
		代码

	elif  表达式 ：
	    代码
	else ：
		代码

	实例1：双分支if
		if _username == username and _password == password:
		    print ("Welcome usuer {name} login...".format(name=username))
		else:
		    print("Invalid username or password!")	

    实例2：单分支if
    	if yy = 17:
    		print("yes,good!")

    实例3：多分支if
		# -*- coding: utf-8 -*-
		# Author:yancy
		age_of_yy = 25
		count = 0
		while count <3:
		    guess_age = int(input("guess age: "))
		    if guess_age == age_of_yy:
		        print("yes,you got it.")
		        break
		    elif guess_age > age_of_yy:
		        print("think smaller...")
		    else:
		        print("think bigger!")
		    count += 1
		    if count ==3:
		        countine_confirm = input("do you want to keep guessing...?")
		        if countine_confirm !='n':
		            count = 0
		else:
		  print("you have trice too many times... godeby!!")   
		
	if嵌套格式：
		if 表达式1:
		    语句
		    if 表达式2:
		        语句
		    elif 表达式3:
		        语句
		    else:
		        语句
		elif 表达式4:
		    语句
		else:
		    语句

		if嵌套实例：
		# !/usr/bin/python3
		 
		num=int(input("输入一个数字："))
		if num%2==0:
		    if num%3==0:
		        print ("你输入的数字可以整除 2 和 3")
		    else:
		        print ("你输入的数字可以整除 2，但不能整除 3")
		else:
		    if num%3==0:
		        print ("你输入的数字可以整除 3，但不能整除 2")
		    else:
		        print  ("你输入的数字不能整除 2 和 3")

循环语句
	for
		for循环的条件是列表不为空就循环，列表为空就退出循环
		实例1：
		for i in range(0,10,2):
    		print("loop",i)

    	实例2：
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

	while
		while循环的的条件是给定的条件为真就循环，为假就退出循环
		实例1：
		for i in range(10):
	    print('------',i)
	    for j in range(10):
	        print (j)
	        if j >5:
	            break

	    实例2：
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

    range()函数
    	如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
    	>>>for i in range(5):
		...   print(i)
		...
		0
		1
		2
		3
		4

	break和continue语句
		break 用于结束当前的循环
		continue 用于跳过当前循环执行下一个循环

	循环中的else子句
		else 用于循环条件不满足或者循环执行完了，将会执行这个

	pass 语句
		pass 不做任何事情，一般用做占位语句，如下实例
		实例：
			#!/usr/bin/python3
			 
			for letter in 'Runoob': 
			   if letter == 'o':
			      pass
			      print ('执行 pass 块')
			   print ('当前字母 :', letter)
			 
			print ("Good bye!")
			执行以上脚本输出结果为：
			当前字母 : R
			当前字母 : u
			当前字母 : n
			执行 pass 块
			当前字母 : o
			执行 pass 块
			当前字母 : o
			当前字母 : b
			Good bye!