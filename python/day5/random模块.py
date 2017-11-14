#!/usr/bin/env python
#!--*-- coding: utf-8 --*--
# Author yancy
import random

# 随机数
print(random.random)
print(random.randint(1,3))
print(random.randrange(1,10))

import random
checkcode = ""
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)