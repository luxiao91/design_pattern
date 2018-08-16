"""饮料相关的基类和几种具体实现
"""
from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def get_desc(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class CoffeeA(Beverage):

    def __init__(self):
        super().__init__()

    def get_desc(self):
        return "CoffeeA"

    def get_cost(self):
        return 0.99


class CoffeeB(Beverage):

    def __init__(self):
        super().__init__()

    def get_desc(self):
        return "CoffeeB"

    def get_cost(self):
        return 1.99
