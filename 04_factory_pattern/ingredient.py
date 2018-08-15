"""原料工厂

采用抽象工厂
"""
from abc import ABCMeta, abstractmethod


class IngredientFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


class NYIngredientFactory(IngredientFactory):

    def __init__(self):
        super().__init__()

    def create_sauce(self):
        return "NY_sauce"

    def create_cheese(self):
        return "NY_cheese"

    def create_dough(self):
        return "NY_dough"

    def create_clam(self):
        return "NY_clam"


class CHIngredientFactory(IngredientFactory):

    def __init__(self):
        super().__init__()

    def create_sauce(self):
        return "CH_sauce"

    def create_cheese(self):
        return "CH_cheese"

    def create_dough(self):
        return "CH_dough"

    def create_clam(self):
        return "CH_clam"
