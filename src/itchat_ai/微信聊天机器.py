#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 3/4/23 12:16 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 微信聊天机器.py
# @Software : PyCharm


import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    reply_text = "我已经收到了你的消息：{}".format(msg['Text'])
    return reply_text


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)  # 热登录，避免重复扫码
    itchat.run()
