#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/11/23 6:11 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 游戏案例.py
# @Software : PyCharm

class Game(object):
    # 定义类属性
    # 历史最高分
    top_score = 0

    def __init__(self, player_name=None):
        # 定义实例属性
        self.player_name = player_name

    @staticmethod
    def show_help():
        # 静态方法显示帮助信息
        print("游戏帮助信息，让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        # 类方法显示历史最高分
        print("历史最高分为 %d" % cls.top_score)

    def start_game(self):
        # 实例方法  实例方法访问实例属性
        print("%s 开始了游戏" % self.player_name)


# 1、查看游戏的帮助信息
Game.show_help()
# 2、查看历史最高分
Game.show_top_score()
# 3、创建游戏对象实例
game = Game("小明")
game2 = Game()
# 对象实例调用实例方法
game.start_game()
game2.start_game()
