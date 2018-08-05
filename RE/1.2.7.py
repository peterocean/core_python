#usr/bin python3
# -*- coding:utf-8 -*-

import re

pattern = '\w+-\d+'

print('match test1: yyf-10601')
m = re.match(pattern, 'yyf-10601')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test2: yyf- 10601')
m = re.match(pattern, 'yyf- 10601')
if m is not None:
    print(m.group())
else:
    print('match none')

print('match test3: @yyf-10601')
m = re.match(pattern, '@yyf-10601')
if m is not None:
    print(m.group())
else:
    print('match none')
