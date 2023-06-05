#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/13/23 11:22 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : openaimode.py
# @Software : PyCharm
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
