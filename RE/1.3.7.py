#/usr/bin python3
#-*- coding:utf-8 -*-

import re

#匹配任何单个字符
pattern = '.end'

print('match test 1:')
m = re.match(pattern, 'bend')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test 2')
m = re.match(pattern, 'end')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test 3')
m = re.match(pattern, '\nend')
if m is not None:
    print(m.group())
else:
    print('match none')

patt314 = '3.14'
pi_patt = '3\.14'

print('match test 4')
m = re.match(patt314, '3.14')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test 5')
m = re.match(patt314, '3014')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test 6')
m = re.match(pi_patt,'3.14')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test 7')
m = re.match(pi_patt, '3014')
if m is not None:
    print(m.group())
else:
    print('match none')

    


             
