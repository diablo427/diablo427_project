#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/1/29 23:08
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : cards_tools.py
# @Software : PyCharm
import cards_tools as ct
while True:
    # todo 展示菜单
    ct.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是：【%s】" % action_str)

    if action_str in ["1", "2", "3","0"]:
        # 新增名片
        if action_str == "1":
            ct.new_card()
        # 显示全部
        elif action_str == "2":
            ct.show_all()
        # 查询名片
        elif action_str == "3":
            ct.search_card()
        elif action_str == "0":
            print("欢迎再次使用【%s】" % ct.cards_system)
            break
    else:
        print("您输入的不正确，请重新选择")
