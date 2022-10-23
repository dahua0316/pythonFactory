#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :11factory.py
# @Time      :2022/10/23 8:51
# @Author    :Dahua

from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):  # 抽象订阅者
    @abstractmethod
    def update(self, notice):  # notice 是一个Notice 对象
        pass


# 抽象发布者
class Notice:
    def __init__(self):
        self.observer = []

    def attach(self, obs):
        self.observer.append(obs)

    def detch(self, obs):
        self.observer.remove(obs)

    def notify(self):
        for obs in self.observer:
            obs.update(self)


# 具体发布者
class StaffNotice(Notice):
    def __init__(self, _company_info=None):
        super().__init__()
        self._company_info = _company_info

    @property
    def company_info(self):
        return self._company_info

    @company_info.setter
    def company_info(self, info):
        self._company_info = info
        self.notify()


# 具体订阅者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


if __name__ == "__main__":
    notice = StaffNotice()
    s1 = Staff()
    s2 = Staff()
    notice.attach(s1)
    notice.attach(s2)
    print(s1.company_info)
    print(s2.company_info)
    notice.company_info = "公司明天放假"
    print(s1.company_info)
    print(s2.company_info)
