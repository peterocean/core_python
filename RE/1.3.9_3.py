#/usr/bin python3
# -*- coding:utf-8 -*-

import re

print('test1:')
pattern = 'ab'
m = re.match(pattern, 'ab')
if m is not None:
    print(m.group())
    print(m.groups())
else:
    print('match none')

print('test2:')
pattern = '(ab)'
m = re.match(pattern, 'ab')
if m is not None:
    print(m.group())
    print(m.groups())
    print(m.groups(1))
else:
    print('match none')
    
print('test3:')
pattern = '(a)(b)'
m = re.match(pattern, 'ab')
if m is not None:
    print(m.group())
    print(m.groups())
    print(m.groups(1))
    print(m.groups(2))
else:
    print('match none')
