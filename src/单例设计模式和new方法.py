#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 6:30 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 单例设计模式和new方法.py
# @Software : PyCharm

# todo 单例模式使用场景
# 1、音乐播放对象
# 2、回收站对象
# 3、打印机对象

# todo __new__方法 object 内置的静态方法
# 1、在内存中为对象 分配空间
# 2、todo 返回对象的引用

# 定义一个播放器类
class MusicPlayer(object):
    # 重写new 方法
    def __new__(cls, *args, **kwargs):
        # 1.创建对象时new方法会自动被调用
        print("创建对象，分配空间")
        # 2.为对象分配空间
        instance = super().__new__(cls)
        # 3.返回对象的引用
        return instance

    # 定义实例初始化方法
    def __init__(self):
        print("播放器初始化")


# 1、创建播放器对象
player = MusicPlayer()
print(player)
