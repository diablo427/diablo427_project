#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 10:44 AM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 查找算法.py
# @Software : PyCharm
def binary_search(arr, x):
    """
    二分查找
    :param arr: 被查找的数组
    :param x: 目标元素
    :return: 查到该元素返回该元素的索引，未查到返回-1
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # //代表向下取整
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in the array")


class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
