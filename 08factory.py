#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :08factory.py
# @Time      :2022/10/15 14:00
# @Author    :Dahua

# 子系统
class Cpu:
    def run(self):
        print('cpu 启动')

    def stop(self):
        print('cpu 关机')


# 子系统
class Disk:
    def run(self):
        print('磁盘启动')

    def stop(self):
        print('磁盘停止')


# 子系统
class Memory:
    def run(self):
        print('内存启动')

    def stop(self):
        print('内存关机')


# 外观类
class Computer:
    def __init__(self):
        self.cpu = Cpu()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


if __name__ == "__main__":
    computer = Computer()
    computer.run()
    computer.stop()
