#/usr/bin python3
#-*- coding:utf-8 -*-

import re

print('match test1: abc-123')
pattern = '(\w\w\w)-(\d\d\d)'
m = re.match(pattern, 'abc-123')
if m is not None:
    print(m.group())
    print(m.groups())
    print(m.group(1))
    print(m.group(2))
else:
    print('match none')

print('match test2: abc-123')
pattern = '(\w\w\w)-(\d\d\d)'
m = re.match(pattern, 'abc123')
if m is not None:
    print(m.group())
    print(m.groups())
    print(m.group(1))
    print(m.group(2))

else:
    print('match none')

    
