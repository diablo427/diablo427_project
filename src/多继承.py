#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/9/23 10:42 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 多继承.py
# @Software : PyCharm

class A:
    def test(self):
        print("a")
class B:
    def test(self):
        print("b")
class C:
    def test(self):
        print("c")
class D(A,C,B):
    pass
# todo 多继承的注意事项：
# todo 如果多个父类中有同名方法，属性，尽量避免使用多继承
d =D()
d.test()
print(D.__mro__)

