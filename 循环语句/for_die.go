package main

import "fmt"

func main() {
	for true {
		fmt.Printf("这是无限循环。\n")
	}
}

//如过循环中条件语句永远不为 false 则会进行无限循环，我们可以通过 for 循环语句中只设置一个条件表达式来执行无限循环：
