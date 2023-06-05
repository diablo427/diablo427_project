#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 10:10 AM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : read_config_prefile.py
# @Software : PyCharm
from configparser import ConfigParser


# def load_config():
config_parser = ConfigParser()
config_parser.read("config.cfg")
mysql_config = config_parser["mysql"]
host = mysql_config['host']
port = mysql_config['port']
charset = mysql_config['charset']
user = mysql_config['user']
password = mysql_config['password']
db = ['test_db']
openai_config = config_parser["OpenAi"]
my_openai_key = openai_config["MyOpenAiKey"]
