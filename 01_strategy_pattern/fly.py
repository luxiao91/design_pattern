"""各种飞的方法
"""
from abc import ABCMeta, abstractmethod


class FlyBehavior(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class FlyWithWings(FlyBehavior):

    @staticmethod
    def fly():
        print("FlyWithWings!")


class FlyNoWay(FlyBehavior):

    @staticmethod
    def fly():
        print("FlyNoWay!")
