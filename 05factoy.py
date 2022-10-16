#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :05factoy.py
# @Time      :2022/10/7 14:25
# @Author    :Dahua

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay:
    def const(self, money):
        print('支付宝支付了%s' % money)


# 方案一 ===类适配了器====

class NewAlipay(Payment, Alipay):
    def pay(self, money):
        self.const(money)


# 方案二 =========对象适配器======

class NewAlipay2:
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.const(money)


if __name__ == "__main__":
    p1 = NewAlipay()
    p1.pay(36)

    p2 = NewAlipay2(Alipay())
    p2.pay(48)
