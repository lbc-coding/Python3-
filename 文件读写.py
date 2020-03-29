#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   文件读写.py
@Time    :   2020/02/09 21:35:35
@Author  :   Liu Baochang 
@Contact :   543730416@qq.com
'''

# here put the import lib
import os

f_name = 'test.txt'
copy_f_name = 'copy.txt'

with open(f_name, 'r') as f:
    b = f.read()
    with open(copy_f_name, 'w') as copy_f:
        copy_f.write(b)

try:
    os.rename(copy_f_name, 'copy2.txt')
except OSError:
    os.remove('copy2.txt')

print(os.listdir(os.curdir))
print(os.listdir(os.pardir))

try:
    os.mkdir('subdir')
except OSError:
    os.rmdir('subdir')

for item in os.walk('.'):
    print(item)

print(os.path.isfile(f_name))