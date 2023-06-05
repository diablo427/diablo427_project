#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/25/23 11:52 AM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 判断是否中文字符.py
# @Software : PyCharm


def is_chinese(str_list):
    """

    :param str_list:
    :return:
    """
    count_chinese = 0
    count_else = 0
    for ch in str_list:
        if '\u4e00' <= ch <= '\u9fff':
            count_chinese += 1
        else:
            count_else += 1
    # print('中文字符为: %d' % count_chinese + '非中文字符为: %d' % count_else)
    return count_chinese, count_else


def ch_list(str):
    begin_index = 0
    end_index = 1
    str_list = []
    while end_index <= len(str):
        str_list.append(str[begin_index:end_index])
        begin_index += 1
        end_index += 1
    return str_list


if __name__ == '__main__':
    str1 = '我是一个小伙伴，你知道吗，xiaohaizi.ddd,'
    s = is_chinese(ch_list(str1))
    print(s)
