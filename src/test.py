#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 18:35
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : test.py
# @Software : PyCharm
import sys
import pandas as pd
import time
import pymysql
from configparser import ConfigParser
import collections
import keyword


# python读取mysql
def load_data_from_mysql1():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="396200", database="test_dev",
                           charset="utf8")
    cursor = conn.cursor()
    des = cursor.description
    sql = '''select * from test;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    print(des)
    print(result)
    # conn.close()
    return result


def load_data_from_mysql2(host, port, user, password, db, charset):
    conn = pymysql.connect(host=host, port=3306, user=user, password=password, db=db, charset=charset)
    cursor = conn.cursor()
    des = cursor.description
    print("step1")
    sql = '''select * from test;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    print(des)
    print(result)
    # return result


# todo read config
def load_config():
    config_parser = ConfigParser()
    config_parser.read("config.cfg")
    config = config_parser["mysql"]
    host = config['host']
    port = config['port']
    charset = config['charset']
    user = config['user']
    password = config['password']
    db = ['test_db']
    print(host + "\t" + port + "\t" + charset + "\t" + user + "\t" + password)
    load_data_from_mysql2(host, port, user, password, db, charset)
    print("error")


# age = int(input("请输入年龄："))
def input_age():
    while True:
        age = int(input("请输入年龄："))
        if age == 0:
            break
        elif age >= 18:
            print("你已成年，欢迎来网吧")
        else:
            print("回家找爹妈")
    print("最终代码")


# 九九乘法表
def multiple_table():
    row = 1

    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d " % (col, row, col * row), end="\t")
            col += 1
        print("")
        row += 1


"""
这是多行注释
信不信
我玩死你
好好学习
天天向上
do you like python
"""

if __name__ == '__main__':
    # load_data_from_mysql1()
    name1 = "小明"
    name2 = "小智"
    a = 10
    # print("我的名字叫 %s，请多多关照，我的名字叫 %s " % (name1, name2))
    scale = 0.25

    print("数据比例是 %.2f%%" % (scale * 100))


    # continue 的用法
    # i = 0
    # while i < 10:
    #     if i == 3:
    #         i += 1
    #         continue  # continue可能会导致死循环
    #     print(i)
    #     i += 1

    def print_line(char, times):
        print(char * times)


    def print_lines(char, times, conts):
        """
        打印多行分割线

        :param char: 要打印的字符
        :param times: 打印的次数
        :param conts: 打印的行数
        """
        row = 0
        while row < conts:
            print_line(char, times)
            row += 1


    print_lines("+", 50, 3)
    tup1 = ("zhangsan", 1, 2, 3, 4, 1)
    list_tup = []
    print(len(tup1))
    print(tup1[5])
    print(tup1[1])

    # for x in tup1:
    #     print(x)
    #     if x == 1:
    #         list_tup.append(tup1.index(1))
    #
    # print(list_tup)
    # 字典遍历
    xiaoming = {"name": "xiaoming", "age": 20, "gender": True}
    for k in xiaoming:
        print("%s -> %s" % (k, xiaoming[k]), end="\t")

    # 列表+字典组合
    xiaohong = {"name": "xiaohong", "age": 21, "gender": False}
    # todo 将同一个对象用一个列表存储,然后对每个对象循环进行同一种操作
    print("")
    card_list = [xiaoming, xiaohong]
    for card in card_list:
        for k in card:
            print("%s -> %s" % (k, card[k]), end="\t")
        print("")
    # 字符串切片
    str1 = "hel0loworld"
    print(str1[0:11:2])
    print(str1[-1::-1])


    def for_function():
        # 完整的for循环语法
        student_name = "小6"
        students = [{"name": "阿土", "age": 20}, {"name": "小四", "age": 20}, {"name": "小美", "age": 20}]
        for student in students:
            if student["name"] == student_name:
                print("找到了 %s" % student_name)
                break
        else:
            print("查找完毕，没有找到 %s" % student_name)

