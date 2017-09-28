#/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:W-D
import sys
sys.setdefaultencoding('utf8')
test="你好"

file = 'ci.txt'
with open(file, 'rt',encoding = 'utf-8') as f:
    data = f.read()
    print(data)