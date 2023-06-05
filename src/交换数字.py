#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 13:35
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 交换数字.py
# @Software : PyCharm
a = 6
b = 100

# 解法一：使用中间变量
# c=a
# a=b
# b=c

# 解法二：不实用其他的变量
# a = a + b
# b = a - b
# a = a - b

# 解法三
# 相当于mapping映射
# a, b = (b, a)
# 简化版
a, b = b, a

print("a= %d ,b = %d" % (a, b))
