"""各种叫的方法
"""
from abc import ABCMeta, abstractmethod


class QuackBehavior(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def quack():
        pass


class Quack(QuackBehavior):

    @staticmethod
    def quack():
        print("Quack!")


class Squeak(QuackBehavior):

    @staticmethod
    def quack():
        print("Squeak!")
