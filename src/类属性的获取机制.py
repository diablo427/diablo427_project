#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 5:36 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 类属性的获取机制.py
# @Software : PyCharm

# todo  向上寻找类属性
class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# 1、创建工具类实例
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
# 2、输出工具类对象总数
# todo 有两种方法1、使用类名.属性（推荐）  2、实例对象.属性
tool2.count = 99
print(Tool.count)
print(tool1.count)
print(tool2.count)
print(tool3.count)
Tool.count = 12
print(Tool.count)
