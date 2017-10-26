package main

import "fmt"

const d int = 1             //定义常量，const关键字 常量名 类型 赋值,这种被称为显示类型定义
const e = true              //定义常量,省略了类型，由系统自动推导,这种被称为隐式类型定义
const f, g, h int = 5, 6, 7 //一次定义多个常量的方法

const ( //一次定义多个常量的又一种方法
	aa     = "jj"
	bb int = 33
	cc     = false
)

const ( //iota,一种特殊的常量，在每一个const关键字出现时，被重置为0，然后再下一个const出现之前，每出现一次iota，其所代表的数字会自动增加1。 iota 可以被用作枚举值
	dd = iota
	ee = iota
	ff = iota
)

const ( //iota枚举的用法，这段常量的声明也可以放到func里面去
	a1 = iota //0
	b1        //1
	c1        //2
	d1 = "ha" //独立值，iota += 1
	e1        //"ha"   iota += 1
	f1 = 100  //iota +=1
	g1        //100  iota +=1
	h1 = iota //7,恢复计数
	i1        //8
)

const ( //常量还可以用作枚举：
	Unknown = 0
	Female  = 1
	Male    = 2
)

func main() {
	const LENGTH int = 10
	const WIDTH = 5
	var area int
	const a, b, c = 1, false, "yuanyang"
	i := 9

	area = LENGTH * WIDTH
	fmt.Printf("面积为 : %d", area)
	println()
	println(a, b, c, d, e, f, g, h, i)
	println(aa, bb, cc)
	println(dd, ee, ff)
	println(Unknown)
	println(Female)
	println(Male)
	println(a1, b1, c1, d1, e1, f1, g1, h1, i1)
}

/*
常量是一个简单值的标识符，在程序运行时，不会被修改的量。
常量中的数据类型只可以是布尔型、数字型（整数型、浮点型和复数）和字符串型。
常量的定义格式：
const identifier [type] = value
你可以省略类型说明符 [type]，因为编译器可以根据变量的值来推断其类型。
显式类型定义： const b string = "abc"
隐式类型定义： const b = "abc"
多个相同类型的声明可以简写为：
const c_name1, c_name2 = value1, value2
*/
