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

	身份运算符：
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

	运算符优先级：
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

字符串：
	字符串是不能修改的，对其的修改操作实际上是在内存中另外开辟了一块地址，和之前的字符串没有关系了。
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




列表：
	列表可以修改，列表可以嵌套列表，字符串，字典等任何东西。
	names = ["袁阳","中国","湖北","襄阳"]

	#查
	print(names)    #取值整个列表
	print(names.index("湖北"))    #查找出列表中的某个值所对应的索引ID
	print(names[names.index("襄阳")])     #根据列表中的索引ID返回所对应的值
	print(names[0])     #取值第一个索引
	print(names[0],names[3])    #取出第一个索引和第四个索引
	print(names[1:3])           #从第二个索引开始取值，到第三个结束，切片不包含最后一个元素，俗称顾头不顾尾
	print(names[-1])            #取切片取值最后一个值,即倒着取
	print(names[-3:-1])         #从倒数第三个开始取值，取到最后一个值。该切片同样不包含最后一个元素
	print(names[-3:])           #从倒数第三个数值开始取值，取到最后一个结束

	#增
	names.append("叶兰")         #追加一个新的值，也就是插入末尾
	print(names)
	names.insert(1,"深圳")        #在列表的第一个索引处插入一个新的值，前面的数字表示索引的位置，后面是对应该索引的值
	print(names)

	#删
	names.remove("叶兰")          #删除值为"叶兰"的值
	print(names)
	del names[1]                #删除列表中第二个索引所对应的值
	print(names)
	names.pop()                 #如果不加数字，默认删除最后一个数值
	print(names)
	names.pop(1)                #删除第二个索引的值
	print(names)
	names.clear()               #清空列表
	print(names)
	# del names                   #删除整个列表


	numbers = [0,1,2,3,4,5,6,7,8,9,"!","yancy","yy","yuanyang","yelan"]
	print(numbers)
	numbers.reverse()            #反转列表,就是讲列表的初始顺序调换一下
	print(numbers)

	nums = [5,1,3,2,4,9,7,0,8,6]
	nums.sort()                 #排序
	print(nums)


	strings = ["yancy","yy","yuanyang","yelan"]
	print(strings)
	strings.reverse()
	print(strings)
	strings.sort()           #自动按照accsis编码排序,特殊字符会优先排序,注意:字符串不能和数字一起排序，会报错
	print(strings)

	numbers.extend(strings)  #扩展列表。可以将其他的列表追加到该列表来.这个表示把string列表增加到numbers列中来
	print(numbers)


	str1 = ["aa","bb","yy","cc",["yuanyang","yelan"]]
	str2 = str1.copy()      #浅拷贝,只拷贝第一层的（即第一层的变量不包括子列表会被独立的开辟一块内存地址），如果列表里面镶嵌了子列表，那么第二层的列表里面的所有数值都会当成一个内存地址（即2个列表共用的同一个内存地址，都把内存指针指向了这个内存地址）
	print(str1)
	print(str2)
	str1[0] = "啊啊"          #修改第一个元素为汉字
	str2[4][1] = "叶兰"       #修改第4个元素的第一个元素为汉字
	print(str1)
	print(str2)


	import sys
	import copy                 #导入模块，说道模块有个sys模块是c语音写的，所以我们在python的环境变量中是无法找到sys.py的模块的
	address_1 = ["北京","上海","广东","湖北","湖南",["袁阳","叶兰"]]
	# address_2 = copy.deepcopy(address_1)     #导入copy模块，用这个模块的深度复制已达到完全的拷贝
	print(address_1)
	# print(address_2)
	address_1[0] = "beijing"
	# address_2[5][1] = "yy"
	print(address_1)
	# print(address_2)

	for i in address_1:
	    print(i)

	num = [1,2,3,4,5,6,7,8,9]
	print(num[0:-1:2])          #打印从第一个元素到倒数第一个元素，即所有元素，并空一格打印一个
	print(num[::2])             #打印所有，并空一格打印一个
	print(num[:])               #如果省略了数字就默认以0开头以-1结尾（即从头到尾的打印）
	print(num[::])              #同上


	person = ["name",["saving",10000]]
	p1 = copy.copy(person)  #扩展中浅拷贝的方式
	p2 = person[:]
	p3 = list(person)
	print(p1)
	print(p2)
	print(p3)

	p1[0] = "yy"
	p2[0] = "yancy"
	p3[0] = "yuanyang"
	print(p1)
	print(p2)
	print(p3)






字典:
    字典是无序的，所以不能用index来查，字典的key唯一的，不能重复。
	# 定义一个字典
	info = {'name':'yy',
	        'heigh':'175',
	        'sex':'man',
	        'hobby':'bike'
	        }

	#查  字典是无序的，所以不能用index来查
	print(info.values())    #打印该字典的所有的value的值
	print(info.keys())      #打印该字典的所有的keys值
	print(info)             #打印字典中的所有内容
	print(info.get('name')) #查找key名称是name所对应的value,如果有就返回其所对应的value,如果没有的话就不输出
	print("address" in info) # 判断info这个字典中是否有adress这个key,如果没有就返回False，如果有就返回Ture，在python2.7中还可以这么写：info.has_key("adress")

	print(info.setdefault("name2","yancy")) #该方法可以去取该字典是否存name这个值，如果存在就会返回后面定义的值，如果不存在就回新建一个key值对
	print(info)

	info.setdefault("place","湖北")       #该方法可以去字典去取相应的Key（place）值，如果没有取到(就说明没有定义这个key)，也就是新建一个新的key值
	print(info)

	#改
	info['name'] = "袁阳"     #修改一个字典中的一个key所对应的value值
	print(info)
	info['age'] = '25'      #如果该字典没有对应的key，就是新增了一个key信息
	print(info)


	#删
	del info["name"]        # 删除该字典中的name这个key
	print(info)
	info.pop("sex")         #删除该字典中的heigh
	print(info)
	info.popitem()          #随机删除该字典的一个Key信息
	print(info)


	#其他
	a = {
	'hobby':'bike',
	'name' : 'yancy',
	'age':'25'
	}
	b = {
	'hobby':'ping-pong',
	1:100,
	2:200
	}

	a.update(b)         ##该方法可以将另外一个字典中的key和value更新到这个字典中，如果出现想用的key的话会用后面的字典中的value进行现有的value.
	print(a)

	c = dict.fromkeys([1,2,2,3,3,4,4],[444,{"name":"yancy"},555])   #这里面有2个列表，会自动将前面的列表去重并将去重后的每一个元素生成一个字典中所对应的key.然后将后面的列表当成一个内存地址同时赋值给没有key的元素
	print(c)

	c[3][1]["name"] = "叶兰"  #如果通过fromkeys定义生成的字典，修改其中任意一个key的值，那么所有的key的value都会跟着变化的.
	print(c)

	# for i in info:          #循环打印字典中的没有个key和value
	#     print(i,info[i])

	for k,v in info.items():    #这个循环会将字典先转换成一个列表，然后再打印出来，如果数据量较小的话和上面的循环的方法差不多，数据量大的时候不要使用
	    print(k,v)


元组：
	元组一经定义不能修改，所以它只有查询的操作
	names = ("yy","yuanyang","linfan","yancy") #定义一个元组，元组支持的方法列表都支持而且元组仅仅支持两种方法
	print(names)
	print(names.count("yancy"))     ##统计字符串在该列表出现的次数,注意：不能把元素中的单个字母拿出来找，要找的字符串必须存在于元素中。
	print(names.index("yancy"))     #超照列表中的某个值所对应的索引ID，这个ID会和第一项匹配，如果出现了就直接匹配出来不会继续往下查找了

集合：
	集合是两个列表之间的关系表达式
	list_1 = [1,3,4,2,1,1,4,5,7,8,9]
	list_1 =  set(list_1)                   #定义一个集合，集合天去重，不会有重复的元素
	print(list_1,type(list_1))

	list_2 = set([2,3,1,3,10,7,444,333])
	print(list_1,list_2)

	#交集
	print(list_1.intersection(list_2))
	print(list_1 & list_2)

	#并集
	print(list_1.union((list_2)))
	print(list_1 | list_2)

	#差集   一个里面有，另一个里面没有的集
	print(list_1.difference(list_2))    #in list_1 but not in list_2
	print(list_2.difference(list_1))    #in list_2 but not in list_1
	print(list_1 - list_2)              ##in list_1 but not in list_2


	#子集
	list_3 = set([1,2])

	print(list_1.issubset(list_2))      #list_1是不是list_2的子集,返回为False
	print(list_1.issuperset(list_2))    #list_1是不是list_2的父集,返回为False

	print(list_3.issubset(list_1))      #list_3是不是list_1的子集,返回为True
	print(list_1.issuperset(list_3))    #list_1是不是list_3的父集,返回为True

	#对称差集   去掉两个集合中的交集后，即去除大家都有的数据，保留一个月，另一个没有的数据。
	print(list_1.symmetric_difference(list_2))
	print(list_1 ^ list_2)

	#增
	list_1.add(777)     #在list_1中添加777
	print(list_1)
	list_1.update([100,200,300])    #添加多个元素
	print(list_1)

	#查
	# 100 in list_1           #判断100在不在list_1这个集合里
	# 200 not in list_1       #判断200是不是不在list_1这个集合里
	print(len(list_1))         #查询列表长度

	#改
	list_1.copy()     #浅复制

	#删
	list_1.remove(100)          #删除指定的元素
	print(list_1,"-----")
	print(list_1.pop())         #随即删除一个元素，并返回删除的元素
	list_1.discard(77)          #discard删除，有就删除，没有也不会报错

条件语句：
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

标准库和第三方库
	标准库：Python自带的库，不用额外安装，一般放在python安装目录下的lib目录下。注意：不要在项目目录里建立一个和标准库的名字相同的文件名，不然在引用标准库的时候系统会默认把这个文件当做自己写的库引用。
	第三方库：需要额外安装，一般放在python安装目录下的Lib\site-packages下。