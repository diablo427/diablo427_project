#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/8/23 9:06 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 继承类.py
# @Software : PyCharm
class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def shut(self):
        print("汪汪汪")
    def eat(self):
        print("吃屎")
        super().eat()
        print("dadasadadada")


class Cat:
    def catch(self):
        print("抓老鼠")


wangchai = Dog()
# wangchai.shut()
wangchai.eat()

