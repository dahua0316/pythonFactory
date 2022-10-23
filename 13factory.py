#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :13factory.py
# @Time      :2022/10/23 10:29
# @Author    :Dahua
from abc import ABCMeta, abstractmethod
from time import sleep


class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):  # 原子操作/钩子操作
        pass

    @abstractmethod
    def repaint(self):  # 原子操作/钩子操作
        pass

    @abstractmethod
    def stop(self):  # 原子操作/钩子操作
        pass

    # 模板方法
    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWinow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("start")

    def repaint(self):
        print(self.msg)

    def stop(self):
        print('stop')


if __name__ == "__main__":
    my = MyWinow('HELLOWORLD')
    my.run()
