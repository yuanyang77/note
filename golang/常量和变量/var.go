package main

import "fmt"

//变量的各种声明方法
var a int = 10 //var关键字 变量名 变量类型 = 变量值
var b bool = true
var c = 20 //var关键字 变量名 =  变量值
var d = false
var e, f, g, h int = 1, 2, 3, 4 //同时给多个变量赋值的第一种方法
var i, j, k = 5, 6, 7           //同时给多个变量赋值的第二种方法,省略了类型。
var (                           //同时声明多个变量
	aa bool
	bb int
	cc float64
	dd uint32
	ff int
)
var aaa, bbb, ccc, ddd int //全局变量可以运行只声明而不使用

func main() {
	var e, f, g = 11, 22, 33 //同时给多个变量赋值的第二种方法,在函数体内，局部变量
	i, j, k := 55, 66, 77    //同时给多个变量赋值的第三种方法,省略var关键字和类型，这种只能在函数体内使用。
	ii := 1.22               //给单个函数赋值省略var关键字和类型的写法。
	var ff int               //先定义一个空的变量，在下一行给这个变量赋值。
	ff = 333
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(f)
	fmt.Println(g)
	fmt.Println(h)
	fmt.Println(i)
	fmt.Println(j)
	fmt.Println(k)
	fmt.Println(ii)
	fmt.Println(aa, bb, cc, dd, ff)
	fmt.Println(a, b, c, d, e, f, g, h, j, k, ii)
}

//Go 标记
//Go 程序可以由多个标记组成，可以是关键字，标识符，常量，字符串，符号。如以下 GO 语句由 6 个标记组成：

//标识符
//标识符用来命名变量、类型等程序实体。一个标识符实际上就是一个或是多个字母(A~Z和a~z)数字(0~9)、下划线_组成的序列，但是第一个字符必须是字母或下划线而不能是数字。

//关键字
//下面列举了 Go 代码中会使用到的 25 个关键字或保留字：

/*
break	default	func	interface	select
case	defer	go	map	struct
chan	else	goto	package	switch
const	fallthrough	if	range	type
continue	for	import	return	var
*/

//除了以上介绍的这些关键字，Go 语言还有 36 个预定义标识符：
/*
append	bool	byte	cap	close	complex	complex64	complex128	uint16
copy	false	float32	float64	imag	int	int8	int16	uint32
int32	int64	iota	len	make	new	nil	panic	uint64
print	println	real	recover	string	true	uint	uint8	uintptr
*/

//程序一般由关键字、常量、变量、运算符、类型和函数组成。
//程序中可能会使用到这些分隔符：括号 ()，中括号 [] 和大括号 {}。
//程序中可能会使用到这些标点符号：.、,、;、: 和 …。
