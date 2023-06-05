#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 12:36
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 面向对象.py
# @Software : PyCharm

# 设计的的三要素：
# 1.类名 满足  大驼峰命名法
# 2.属性 这类事物具有什么特性
# 3.方法 这类事物具有什么样的行为
# 大驼峰命名法： CapWords
# 1.每一个单词 的首字母大写
# 2.单词之间没有下划线

class Cat:
    """
    这是一个猫类
    """

    def __init__(self, name=None):
        """
        类的属性封装在该方法中
        :param name: 调用类对象时传入该属性，可设置为缺省值
        """
        print("这是一个初始化方法")
        self.name = name

    def __del__(self):
        print("%s 我去了" % self.name)
        pass

    def eat(self):
        """

        :return:
        """
        print(" %s 爱吃鱼" % self.name)

    def drink(self):
        """

        :return:
        """
        print(" %s 爱喝水" % self.name)


tom = Cat("tom")
tom.eat()
tom.drink()

print(tom)
del tom
lazzy_cat = Cat("大懒猫")
lazzy_cat.eat()
lazzy_cat.drink()
print(lazzy_cat)
lazzy_cat2 = lazzy_cat
print(lazzy_cat2)
rubut_cat = Cat()
rubut_cat.eat()
rubut_cat.drink()
