#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :09factory.py
# @Time      :2022/10/16 11:20
# @Author    :Dahua
import time
from abc import ABCMeta, abstractmethod


# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_contect(self):
        pass

    @abstractmethod
    def set_contect(self):
        pass


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'r', encoding='utf-8')
        self.contect = f.read()
        f.close()

    def get_contect(self):
        return self.contect

    def set_contect(self, contect):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(contect)
        f.close()


# 虚拟代理
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.sub = None

    def get_contect(self):
        if not self.sub:
            self.sub = RealSubject(self.filename)
        return self.sub.get_contect()

    def set_contect(self, contect):
        if not self.sub:
            self.sub = RealSubject(self.filename)
        self.sub.set_contect(contect)

#保护代理
class ProtectedRroxy(Subject):
    def __init__(self,filename):
        self.sub = RealSubject(filename)
    def get_contect(self):
        return self.sub.get_contect()
    def set_contect(self,contect):
        raise PermissionError('无写入权限')

if __name__ == "__main__":
    # 直接调用会生成很大的对象在init 中
    # realsub=RealSubject('Test.txt')
    # realsub.set_contect('hellworld')
    # time.sleep(3)
    # print(realsub.get_contect())

    # 使用虚拟代理创建对象
    # virreadsub = VirtualProxy('Test.txt')
    # virreadsub.get_contect()
    # time.sleep(3)
    # virreadsub.set_contect('helloworld1')

   prorealproxy = ProtectedRroxy('Test.txt')
   print(prorealproxy.get_contect())
   prorealproxy.set_contect('test')