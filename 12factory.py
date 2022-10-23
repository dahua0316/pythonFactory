#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :12factory.py
# @Time      :2022/10/23 9:54
# @Author    :Dahua

from abc import ABCMeta, abstractmethod


# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, date):
        pass


# 具体策略
class FastStrategy(Strategy):
    def execute(self, date):
        print("用较快的策略处理%s" % date)


# 具体策略
class SlowStrategy(Strategy):
    def execute(self, date):
        print("使用较慢的策略处理%s" % date)


class Context:
    def __init__(self, stragegy, date):
        self.date = date
        self.stragegy = stragegy

    def set_stragegy(self, stragegy):
        self.stragegy = stragegy

    def do_stragegy(self):
        self.stragegy.execute(self.date)


if __name__ == "__main__":
    # Client

    date = "[.....]"
    fast = FastStrategy()
    slow = SlowStrategy()
    contect = Context(fast, date)
    contect.do_stragegy()
    contect.set_stragegy(slow)
    contect.do_stragegy()
