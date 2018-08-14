#/usr/bin python3
#-*- coding:utf-8 -*-

import re

print('match test1:first match')
patt = '^the'
m = re.match(patt, 'the dog')
if m is not None:
    print(m.group())
else:
    print('match none')

    
print('match test2:first match')
patt = '^the'
m = re.match(patt, 'dog the end')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test3:end match')
patt = 'the$'
m = re.search(patt, 'dogthe')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test4:end match')
patt = 'the$'
m = re.search(patt, 'dogthe ')
if m is not None:
    print(m.group())
else:
    print('match none')
