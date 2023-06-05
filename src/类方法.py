#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 5:50 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 类方法.py
# @Software : PyCharm


class Tool(object):
    # 定义类属性
    count = 0

    # 定义类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象实例的数量为 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# 创建工具对象实例
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()