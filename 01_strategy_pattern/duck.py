"""Duck主文件

主要包含Duck类以及各种小duck
"""
from abc import ABCMeta, abstractmethod

from quack import QuackBehavior, Quack, Squeak
from fly import FlyBehavior, FlyWithWings, FlyNoWay


class Duck(metaclass=ABCMeta):
    """鸭子抽象类

    因为不能像java一样进行变量声明
    所以在更改属性时限定值类型
    """

    def __init__(self):
        self._quack_behavior = None
        self._fly_behavior = None

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior):
        if not isinstance(quack_behavior, QuackBehavior):
            raise TypeError(
                "Error: quack_behavior should be QuackBehavior."
            )
        self._quack_behavior = quack_behavior

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior):
        if not isinstance(fly_behavior, FlyBehavior):
            raise TypeError(
                "Error: fly_behavior should be FlyBehavior."
            )
        self._fly_behavior = fly_behavior

    @staticmethod
    @abstractmethod
    def display():
        """个体差异方法，直接抽象
        """
        pass

    @staticmethod
    def swim():
        """假设所有鸭子都会游泳
        """
        print("All duck can swim")

    def quack(self):
        """调用子类设定
        """
        self.quack_behavior.quack()

    def fly(self):
        """调用子类设定
        """
        self.fly_behavior.fly()


class RubberDuck(Duck):

    def __init__(self, ):
        super().__init__()
        self.quack_behavior = Squeak()
        self.fly_behavior = FlyNoWay()

    @staticmethod
    def display():
        print("A RubberDuck!")


class WildDuck(Duck):

    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    @staticmethod
    def display():
        print("A WildDuck!")
