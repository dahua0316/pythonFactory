#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :01factory.py
# @Time      :2022/9/24 19:46
# @Author    :Dahua

from abc import ABCMeta, abstractmethod


class People:
    @abstractmethod
    def life(self):
        pass


class Man(People):
    def __init__(self, surperMan = False):
        self.surperMan = surperMan

    def life(self):
        if self.surperMan:
            print('surperman')
        else:
            print('man')


class Woman(People):
    def life(self):
        print('woman')


# 工厂接口
class PeopleFactoryPlus(metaclass=ABCMeta):
    @abstractmethod
    def creatPeople(self):
        pass


# 创建man工厂类
class ManFactory(PeopleFactoryPlus):
    def creatPeople(self):
        return Man()


# 创建woman工厂类
class WomanFactory(PeopleFactoryPlus):
    def creatPeople(self):
        return Woman()


# 创建surpurman工厂类
class surpermanFactory(PeopleFactoryPlus):
    def creatPeople(self):
        return Man(surperMan=True)


class PeopleFactory:
    def createPeople(self, name):
        if name == 'man':
            return Man()
        elif name == 'woman':
            return Woman()
        else:
            raise TypeError('传入%s参数错误' % name)


if __name__ == "__main__":
    # 创建man
    manfactory = ManFactory()
    man = manfactory.creatPeople()
    man.life()
    # 创建woman
    womanfacoty = WomanFactory()
    woman = womanfacoty.creatPeople()
    woman.life()
    # 创建surperman
    surperfactory = surpermanFactory()
    surperman = surperfactory.creatPeople()
    surperman.life()
