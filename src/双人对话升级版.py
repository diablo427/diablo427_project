#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 10:27 AM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 双人对话升级版.py
# @Software : PyCharm
class Person:
    def __init__(self, name):
        self.name = name
        self.conversation_history = []

    def say(self, message):
        print(f"{self.name}: {message}")
        self.conversation_history.append(f"{self.name}: {message}")

    def listen(self, other_person):
        message = input(f"{other_person.name}: ")
        self.conversation_history.append(f"{other_person.name}: {message}")
        return message

    def show_history(self):
        # print("Conversation history:")
        for message in self.conversation_history:
            print(message)

person1 = Person("Person 1")
person2 = Person("Person 2")

while True:
    person1.say(person2.listen(person1))
    person2.say(person1.listen(person2))
