"""配料，用于包装饮料，返回饮料的实例
"""
from beverage import Beverage


class Condiment(Beverage):

    def __init__(self, beverage):
        super().__init__()
        self._beverage = beverage


class MilkA(Condiment):

    def __init__(self, beverage):
        super().__init__(beverage)

    def get_desc(self):
        return self._beverage.get_desc() + " MilkA"

    def get_cost(self):
        return self._beverage.get_cost() + 1


class MilkB(Condiment):

    def __init__(self, beverage):
        super().__init__(beverage)

    def get_desc(self):
        return self._beverage.get_desc() + " MilkB"

    def get_cost(self):
        return self._beverage.get_cost() + 5
