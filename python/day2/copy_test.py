#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:yancy

import copy

person = ['name',['a',100]]
'''
# p1 = copy.copy(person)
# p2 = person[:]
# p3 = list(person)
'''
p1 = person[:]
p2 = person[:]

p1[0] = "yy"
p2[0] = "yelan"
p1[1][1] = 1000000000000000

print(p1)
print(p2)