"""披萨商店

采用工厂方法
"""
from abc import ABCMeta, abstractmethod

from pizza import CheesePizza, ClamPizza
from ingredient import NYIngredientFactory, CHIngredientFactory


class PizzaStore(metaclass=ABCMeta):

    def __init__(self):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.display()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        """工厂方法
        """
        pass


class NYPizzaStore(PizzaStore):

    def __init__(self):
        super().__init__()
        self.ingredient_factory = NYIngredientFactory()

    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza(self.ingredient_factory)
        elif pizza_type == "clam":
            return ClamPizza(self.ingredient_factory)


class CHPizzaStore(PizzaStore):

    def __init__(self):
        super().__init__()
        self.ingredient_factory = CHIngredientFactory()

    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza(self.ingredient_factory)
        elif pizza_type == "clam":
            return ClamPizza(self.ingredient_factory)
