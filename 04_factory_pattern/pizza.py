"""披萨
"""
from abc import ABCMeta, abstractmethod


class Pizza(metaclass=ABCMeta):

    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.cheese = ""
        self.clam = ""

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Bake!")

    def display(self):
        print(" ".join([
            self.name,
            self.dough,
            self.sauce,
            self.cheese,
            self.clam
        ]))


class CheesePizza(Pizza):

    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):

    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.clam = self.ingredient_factory.create_clam()
