package main

import "fmt"

func main() {
	/* 定义局部变量 */
	var a int = 10

	/* for 循环 */
	for a < 20 {
		fmt.Printf("a 的值为 : %d\n", a)
		a++
		if a > 15 {
			/* 使用 break 语句跳出循环 */
			break
		}
	}
}

//用于循环语句中跳出循环，并开始执行循环之后的语句。
//break在switch（开关语句）中在执行一条case后跳出语句的作用。
//语法
//break 语法格式如下：
//break;
