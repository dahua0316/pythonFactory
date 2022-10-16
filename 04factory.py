#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :04factory.py
# @Time      :2022/10/4 9:21
# @Author    :Dahua

class Singleton:
    # 实例化之前执行的函数
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            print('我没有_insstance')
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Myclass(Singleton):
    def __init__(self, a):
        self.a = a


if __name__ == "__main__":
    a = Myclass(10)
    print(a.a)
    b = Myclass(20)
    print(a.a)
    print(b.a)
