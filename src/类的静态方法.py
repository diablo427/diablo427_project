#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 6:01 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 类的静态方法.py
# @Software : PyCharm


class Dog(object):
    # 静态方法
    @staticmethod
    def run():
        """
        不访问类属性，也不访问实例属性
        :return:
        """
        print("小狗要跑。。。。")

    @classmethod
    def shut(cls):
        """
        只访问类属性，不访问实例属性
        :return:
        """
        print("小狗要叫。。。。")

    # 实例方法
    def sleep(self):
        print("小狗要睡觉。。。。")


#  调用类的静态方法 todo 类名.静态方法名（类似于类方法的调用）
Dog.run()
# 调用类方法
Dog.shut()
# todo 实例方法不能被类直接调用
# Dog.sleep()
