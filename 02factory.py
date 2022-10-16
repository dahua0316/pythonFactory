#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :02factory.py
# @Time      :2022/10/3 8:34
# @Author    :Dahua


from abc import ABCMeta, abstractmethod


# ---------------抽象产品接口-------------------

class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def phoneshell_show(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def cpu_show(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def os_show(self):
        pass


# ---------------抽象工厂接口----------------------

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    def make_os(self):
        pass

    def make_cpu(self):
        pass


# ------------------具体产品类-----------------------

class IosPhoneShell(PhoneShell):
    def phoneshell_show(self):
        print('我是iOS手机壳')


class AndroidPhoneShell(PhoneShell):
    def phoneshell_show(self):
        print('我是Android手机壳')


class IosCPU(CPU):
    def cpu_show(self):
        print('我是iOS CPU')


class AndroidCPU(CPU):
    def cpu_show(self):
        print('我是Android CPU')


class IosOS(OS):
    def os_show(self):
        print('我是iOS 系统')


class AndroidOS(OS):
    def os_show(self):
        print('我是Android 系统')


# ------------------具体工厂类-----------------------

class IOSFactory(PhoneFactory):
    def make_shell(self):
        return IosPhoneShell()

    def make_os(self):
        return IosOS()

    def make_cpu(self):
        return IosCPU()


class AndroidFactory(PhoneFactory):
    def make_shell(self):
        return AndroidPhoneShell()

    def make_os(self):
        return AndroidOS()

    def make_cpu(self):
        return AndroidCPU()


# --------------------客户端调用------------------------
class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        print('手机信息：')
        print(self.shell.phoneshell_show())
        print(self.cpu.cpu_show())
        print(self.os.os_show())


def make_phone(factory):
    shell = factory.make_shell()
    os = factory.make_os()
    cpu = factory.make_cpu()
    phone = Phone(shell, cpu, os)
    phone.show_info()


if __name__ == "__main__":
    make_phone(IOSFactory())
    make_phone(AndroidFactory())
