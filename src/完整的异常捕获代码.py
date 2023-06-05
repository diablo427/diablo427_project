#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/13/23 12:11 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 完整的异常捕获代码.py
# @Software : PyCharm
#


# 1、定义一个输入密码的方法
def input_password():
    password = input("请输入8位数密码：")
    # 如果密码长度大于等于8位：密码输入正确
    if len(password) >= 8:
        print("您输入的密码为： %s" % password)
    # 密码小于8位，密码长度不够，主动抛出异常
    else:
        print("主动抛出异常")
        ex = Exception("密码长度不够")
        raise ex
        # print("密码长度不够，请重新输入密码：")
        # input_password()


# 2、调用输入密码的方法
try:
    input_password()
except Exception as result:
    print("捕获到一个异常  %s" % result)
