#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :06factory.py
# @Time      :2022/10/7 15:10
# @Author    :Dahua

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self,color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Green(Color):
    def paint(self, shape):
        print('绿色的%s' % shape.name)


class Rectang(Shape):
    name = "三角形"
    def draw(self):
        self.color.paint(self)


if __name__ == "__main__":
    rectang = Rectang(Green())
    rectang.draw()
