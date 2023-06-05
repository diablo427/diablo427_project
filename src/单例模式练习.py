#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 6:51 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 单例模式练习.py
# @Software : PyCharm

# todo 初始化方法执行一次
class MusicPlayer(object):
    # 定义一个类属性
    instance = None
    # 1、定义类对象的初始化标志
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print("单例模式，重写new方法")
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2、调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3、返回类属性保存的对象引用
        # todo python 中return 不能省略
        return cls.instance

    def __init__(self):
        # 1、判断是否执行过初始化动作
        if MusicPlayer.init_flag is True:
            return
            # 2、如果没有执行过，再执行初始化动作
        print("播放器初始化方法")
        # 3、修改初始化标志的标记
        MusicPlayer.init_flag = True

    # 创建多个对象


player1 = MusicPlayer()
player2 = MusicPlayer()
print("%s 一的地址为" % player1)
print("%s 一的地址为" % player2)
