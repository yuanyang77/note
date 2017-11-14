#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
#1 import导入内置函数用法展示:
import sys,os
print(os.path.abspath(__file__))    #打印当前脚本的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))   #打印当前脚本所在目录的绝对路径


#2 import导入第三方模块(paramiko连接服务器)的用法展示
import parmiko         #通过用户名密码的方式登陆服务器并执行指令操作如下：
ssh = parmiko.SSHClient()
ssh.set_missing_host_key_policy(parmiko.AutoAddPolicy())
ssh.connect('172.16.1.11',22,'yy','linfan77')
stdin,stdout,stderr = ssh.exec_command('df -Th')
print(stdout.read())
ssh.close()


# 3 Python Package包的导入方法：
# 如何区分你看到的目录是一个Python Package包呢？其实很简单，你只要看这个目录下是否有__init__.py这个文件就好了。
# 如果有那么就是Python Package包，如果没有，就是个普通的目录。
# Foo/
# |-- bin/
# |   |-- foo
# |
# |-- core/
# |   |-- tests/
# |   |   |-- __init__.py
# |   |   |-- test_main.py
# |   |
# |   |-- __init__.py
# |   |-- main.py
# |
# |-- conf/
# |   |-- setting.py
# |   |-- __init__.py
# |
# |-- docs/
# |   |-- conf.py
# |   |-- abc.rst
# |
# |-- setup.py
# |-- requirements.txt
# |-- README
# |
# |-- logs/

# bin/: 存放项目的一些可执行文件，当然你可以起名script/之类的也行。
# foo/: 存放项目的所有源代码。(1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。(2) 其子目录tests/存放单元测试代码； (3) 程序的入口最好命名为main.py。
# docs/: 存放一些文档。
# setup.py: 安装、部署、打包的脚本。
# requirements.txt: 存放软件依赖的外部Python包列表。
# README: 项目说明文件。