#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/9/23 10:25 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 父类的私有属性和方法.py
# @Software : PyCharm
class A:
    def __init__(self):
        """
        常规属性
        """
        self.num1 = 100
        # 私有属性

        self.__num2 = 200

    def __test(self):
        """
        私有方法
        :return:
        """
        print("私有方法 %d %d" % (self.num1, self.__num2))


class B(A):
    pass


b = B()
print(b)

# print(b.__num2) 子类不能调用父类的私有属性
# b.__test()  子类不能调用父类的私有方法
# todo 子类可以调用父类的公有属性和公有方法
# todo 父类在自己的公有方法中调用自己的私有属性和私有方法，子类调用父类的该公有方法时，是合法的。
