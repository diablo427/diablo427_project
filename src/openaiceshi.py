#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/10/23 4:51 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : openaiceshi.py
# @Software : PyCharm

# todo  密钥 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


import os
import openai
# 设置API密钥
openai.api_key = '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'
# openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)
print(completion.choices[0].message)
print(openai.model.list())

