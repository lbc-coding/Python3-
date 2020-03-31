# !/user/bin/env python3.7
# -*- coding:utf-8 -*-
# @Time     : 2020/1/28 5:03 下午
# @Author   : Baochang liu
# @User     : gj
# @File     : 正则表达式.py
# @Software : PyCharm

# 正则表达式 Regular Expression ，常常简写为Regex、re等，可以匹配、查找、替换符合"规则"的字符串。

# 正则表达式，包含普通字符串和元字符串，普通字符串表示字符的原始意思，元字符串是预先定义好的特定字符串。

# 元字符串又包含基础元字符串和普通字符组成。有14个基础元字符串。

# 元字符串是学习重点。
'''开始
    与
    结束字符'''

import re

p = r'[Jj]ava'
text = 'I like Java and java.'
regex = re.compile(p)

m = regex.search(text)
print(m)

m_findall = regex.findall(text)
print(m_findall)

m_finditer = regex.finditer(text)
for m in m_findall:
    print(m)

# git test