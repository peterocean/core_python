#usr/bin python3
#-*- coding:utf-8 -*-


import re

patt1 = '\w+@\w+\.com'
patt2 = '\w+@(\w+\.)?\w+\.com'

print('patt test1: nobody@xxx.com')
m = re.match(patt1,'nobody@xxx.com')
if m is not None:
    print(m.group())
else:
    print('patter match none')

print('patt test2: nobody@www.xxx.com')
m = re.match(patt1,'nobody@www.xxx.com')
if m is not None:
    print(m.group())
else:
    print('patter match none')


print('patt test3: nobody@xxx.com')
m = re.match(patt2,'nobody@xxx.com')
if m is not None:
    print(m.group())
else:
    print('patter match none')

print('patt test4: nobody@www.xxx.com')
m = re.match(patt2,'nobody@www.xxx.com')
if m is not None:
    print(m.group())
else:
    print('patter match none')
