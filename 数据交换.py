#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   数据交换.py
@Time    :   2020/02/09 23:39:01
@Author  :   Liu Baochang 
@Contact :   543730416@qq.com
'''

# here put the import lib
import csv

with open("books.csv", 'r', encoding='gbk') as rf:
    reader = csv.reader(rf, dialect=csv.excel)
    for row in reader:
        print('|'.join(row))