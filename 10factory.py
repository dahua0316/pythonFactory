#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :10factory.py
# @Time      :2022/10/16 14:45
# @Author    :Dahua

from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):
    def handle_leave(self, day):
        if day < 10:
            print("总经理准假%d天" % day)
        else:
            print("你还是离职吧")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day < 5:
            print("部门主管准假%d天" % day)
        else:
            print("部门主管权力不够")
            self.next.handle_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day < 3:
            print('项目主管准假%d' % day)
        else:
            print("项目主管权力不够")
            self.next.handle_leave(day)


if __name__ == "__main__":
    day = 10
    h = ProjectDirector()
    h.handle_leave(day)


