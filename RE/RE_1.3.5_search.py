#/usr/bin python3
# -*- coding:utf-8 -*-

import re

pattern = 'foo'
m = re.search(pattern,'seafood')
print(m)
print(m.group())

m = re.search(pattern, 'seafood seafood')
print(m.group())
