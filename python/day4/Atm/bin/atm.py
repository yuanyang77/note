#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
#跨目录调用
import os
import sys

# print(__file__)
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
from conf import setting
from core import main
main.login()
# import conf,core
