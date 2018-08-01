#/usr/bin python3
#-*- coding:utf-8 -*-

import re

print('match test1')
pattern = 'bat|bet|bit'
m = re.match(pattern, 'bat')
if m is not None:
    print(m.group())
else:
    print("match none")
    
print('match test2')
m = re.match(pattern, 'batbet')
if m is not None:
    print(m.group())
else:
    print("match none")


print('search test1')
pattern = 'bat|bet|bit'
m = re.search(pattern, 'betbat')
if m is not None:
    print(m.group())
else:
    print("match none")
