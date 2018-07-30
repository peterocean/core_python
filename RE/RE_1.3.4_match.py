#/usr/bin python3
# -*- coding:utf-8 -*-

import re

m = re.match('foo','foo')
if m is not None:
    print(m.group())
    print(m.groups())
else:
    print('RE match none')

m = re.match('foo','fun')
if m is not None:
    print(m.group())
    print(m.groups())
else:
    print('RE match none')


RE_pattern_str = 'bat|bet|bit'
SRCstr = 'bat'
m = re.match(RE_pattern_str,SRCstr)
if m is not None:
    print(m.group())
else:
    print('RE match source string none')
