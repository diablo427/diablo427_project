#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/9/23 11:07 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 面向对象的多态.py
# @Software : PyCharm

# todo 多态 不同的子类调用相同的 父类方法，产生不同的执行结果
class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 玩耍" % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s 到天上玩" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        # 让狗玩
        dog.game()

# 1、创建狗对象
wangchai =Dog("旺柴")
xiaotianquan = XiaoTianQuan("啸天犬")
# 2、创建小明对象
xiaoming=Person("小明")
# 3、让小明和狗玩
xiaoming.game_with_dog(wangchai)
xiaoming.game_with_dog(xiaotianquan)
