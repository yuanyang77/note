#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
#跨目录调用
import os
import sys

# print(__file__)	获取当前文件所在目录
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))	#获取当前文件所在目录的上一层目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))	#这个是Atm目录

sys.path.append(BASE_DIR)
from conf import setting
from core import main
main.login()
# import conf,core
