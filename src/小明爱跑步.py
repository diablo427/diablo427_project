#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 14:23
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 小明爱跑步.py
# @Software : PyCharm

class Person:
    """

    """

    def __init__(self, name=None, weight=50.00):
        """

        :param name:
        :param weight:
        """
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 体重是%.2f kg" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print("%s 喜欢跑步，每跑一次体重减少 0.5 kg"%self.name)

    def eat(self):
        self.weight += 1
        print("%s 喜欢吃，体重增加 1 kg" %self.name)


xiao_ming = Person(name="小明", weight=75)
xiao_ming.eat()
xiao_ming.run()
print(xiao_ming)
xiao_mei = Person(name="小美", weight=45)
xiao_mei.eat()
xiao_mei.run()
print(xiao_mei)
