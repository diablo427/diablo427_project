#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 12:50
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 全局变量的修改.py
# @Software : PyCharm
"""在开发时，应该把模块中的所有全局变量定义在所有函数上方
全局变量的命名规范： g_   或者  gl_ """
num = 10


def demo1():
    global num
    num = 99
    print("demo01==> %d" % num)


def demo2():
    num = 100
    print("demo02==> %d" % num)


def demo3():
    print("demo03==> %d" % num)


if __name__ == '__main__':
    # 在函数内修改了全局变量后，全局变量会生效
    demo1()
    demo2()
    demo3()
print(num)
