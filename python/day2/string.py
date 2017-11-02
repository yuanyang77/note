#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:yancy

name = "my \tname is yancy"
print(name.capitalize())
print(name.count("a"))
print(name.center(50,'-'))
print(name.endswith("y"))
print(name.expandtabs(tabsize=30))
print(name.find("name"))
print(name[name.find("name"):])

print('+'.join(['1','2','3']))
