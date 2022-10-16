#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :interfaceTest.py
# @Time      :2022/9/24 12:55
# @Author    :Dahua

from abc import ABCMeta, abstractmethod


# 接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print('支付宝支付%d元' % money)


class Wechatpay(Payment):
    def pay(self, money):
        print('微信支付%d元' % money)


if __name__ == "__main__":
    p = Alipay()
    p.pay(100.01)

    wp = Wechatpay()
    wp.pay(200)


