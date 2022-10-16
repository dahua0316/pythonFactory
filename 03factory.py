#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :03factory.py
# @Time      :2022/10/3 15:40
# @Author    :Dahua


from abc import ABCMeta, abstractmethod


# --------------------具体产品--------------------------

class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return 'face:%s body:%s arm:%s leg:%s' % (self.face, self.body, self.arm, self.leg)


# --------------------抽象工厂接口类----------------------

class PlayBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


# ======================具体工厂类==========================
class SexyGrilBuilder(PlayBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '漂亮的脸蛋'

    def build_body(self):
        self.player.body = '苗条'

    def build_arm(self):
        self.player.arm = '长长的胳膊'

    def build_leg(self):
        self.player.leg = '大长腿'


class Monster(PlayBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '可怕的脸蛋'

    def build_body(self):
        self.player.body = '壮壮的身体'

    def build_arm(self):
        self.player.arm = '胖胖的胳膊'

    def build_leg(self):
        self.player.leg = '短短的腿'


# ============================指挥者进行装配控制顺序========================

class PlayerDirector:
    def build_player(self, builder):
        builder.build_face()
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        return builder.player


if __name__ == "__main__":
    director = PlayerDirector()
    girl = director.build_player(SexyGrilBuilder())
    monstors = director.build_player(Monster())
    print(girl)
    print(monstors)
