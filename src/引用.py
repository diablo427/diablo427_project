#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 11:11
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 引用.py
# @Software : PyCharm
def test(num):
    result = "hello"
    print("在函数内部 %d 对应的地址是 %d" %(num,id(num)))
    print("在函数内部 %s 对应的地址是 %d" %(result,id(result)))
    return result

# 1.定义一个数字变量
a=10
# 数据的地址本质上就是一个数字
print("a 变量保存数据的内存地址是 %d" %id(a))
test(a)
print(id("hello"))




