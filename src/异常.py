#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 7:18 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 异常.py
# @Software : PyCharm
try:
    num = int(input("请输入一个整数："))
    print("输入的数为：%d" % num)
except ValueError:
    print("请输入正确的整数：")
except Exception as result:
    print("未知错误 %s" % result)
