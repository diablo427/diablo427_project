#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/1/29 23:08
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : cards_tools.py
# @Software : PyCharm
cards_system = "名片管理系统"
# 记录所有的名片字典
card_list = []


def show_menu():
    """系统展示菜单"""
    print("*" * 50)
    print("欢迎使用%s" % cards_system)
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)

    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱：")
    # 2.使用用户输入信息建立一个名片字典
    card_dict = {"name": name_str, "phone": phone_str, "qq": qq_str, "email": email_str}
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户添加成功
    print("添加%s的名片成功！" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    if len(card_list) == 0:
        print("当前名片为空，请使用1新增名片")
        return
    # 打印表头
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    print("")
    # 打印分割线
    print("=" * 50)
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (
            card_dict["name"],
            card_dict["phone"],
            card_dict["qq"],
            card_dict["email"]
        ))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("查询名片")
    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了 %s" % find_name)
            # 打印表头
            for name in ["姓名", "电话", "qq", "邮箱"]:
                print(name, end="\t\t")
            print("")
            # 打印分割线
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (
                card_dict["name"],
                card_dict["phone"],
                card_dict["qq"],
                card_dict["email"]
            ))
            # todo 针对找到的名片执行修改和删除的操作
            deal_card(card_dict)
            break
    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    else:
        print("没有找到 %s" % find_name)


def deal_card(card_dict):
    action_str = input("请输入要执行的操作：[1] 修改 [2] 删除 [0] 返回上一层菜单")
    if action_str == "1":
        print("修改名片")
        card_dict["name"] = input_card_info(card_dict["name"], "请输入要修改的姓名：")
        card_dict["phone"] = input_card_info(card_dict["phone"], "请输入要修改的电话：")
        card_dict["qq"] = input_card_info(card_dict["qq"], "请输入要修改的qq：")
        card_dict["email"] = input_card_info(card_dict["email"], "请输入要修改的email：")
        print("修改名片 %s 成功" % card_dict["name"])

    elif action_str == "2":
        print("删除名片")
        card_list.remove(card_dict)
        print("删除 %s 名片成功" % card_dict)


def input_card_info(dict_value, tip_message):
    """

    :param dict_value:
    :param tip_message:
    :return:
    """
    input_str = input(tip_message)
    if len(input_str) == 0:
        return dict_value
    else:
        return input_str
