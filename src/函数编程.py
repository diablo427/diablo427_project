#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 13:43
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 函数编程.py
# @Software : PyCharm
""" 加等于 """


# 函数内部对全局可变变量操作会影响全局可变变量的值
# 函数内部对全局不可变量的操作不会影响该全局变量的值
# 对列表变量相当于调用列表的 extend 方法
# 函数的递归
def sum_numbers(num):
    """
    加法递归函数
    :param num:
    :return:
    """
    if num == 1:
        return 1
    return num + sum_numbers(num - 1)


# print(sum_numbers(3))

def factorial_numbers(num):
    """
    阶乘函数
    :param num:
    :return:
    """
    # 1.函数出口
    if num == 0:
        return 1
    else:
        return num * factorial_numbers(num - 1)

# print(Factorial_numbers(3))
