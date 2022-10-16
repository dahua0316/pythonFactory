#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :07factory.py
# @Time      :2022/10/15 12:50
# @Author    :Dahua


from abc import ABCMeta, abstractmethod


# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # print 打印这个类 会调用这个方法
    def __str__(self):
        return '点（%s,%s）' % (self.x, self.y)

    def draw(self):
        print("================点==================")
        print(str(self))
        print("================点==================")


# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2

    def __str__(self):
        return '线段[%s ,%s]' % (self.x, self.y)

    def draw(self):
        print("================线==================")
        print(str(self))
        print("================线==================")


# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("================复合图形==================")
        for g in self.children:
            g.draw()
        print("================复合图形==================")


if __name__ == "__main__":
    p1 = Point(3, 6)
    l1 = Line(Point(2, 6), Point(3, 6))
    l2 = Line(Point(1, 6), Point(5, 9))
    pic1 = Picture([p1, l1, l2])
    pic1.draw()

    pic2=Picture([pic1])
    pic2.draw()