#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 9:50 AM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 双人对话.py
# @Software : PyCharm
import openai
import read_config_prefile as rp

# 设置API Key
openai.api_key = rp.my_openai_key


# 定义对话函数
def chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


# 开始对话
print("Person 1: Hi, how are you doing today?")
response = chat("Person 2: ")
print("Person 2: " + response)

while True:
    response = chat("Person 1: ")
    print("Person 1: " + response)
    response = chat("Person 2: ")
    print("Person 2: " + response)
