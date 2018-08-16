"""各种叫的方法
"""
from abc import ABCMeta, abstractmethod


class QuackBehavior(metaclass=ABCMeta):

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
