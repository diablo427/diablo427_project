#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 10:38 AM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 排序算法.py
# @Software : PyCharm
def quick_sort(arr):
    """
    快排
    :param arr:排序前的数组
    :return:排序后的数组
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def bubble_sort(arr):
    """
    冒泡排序
    :param arr: 排序前的数组
    :return: 排序后的数组
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """
    插入排序
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
