"""装饰者模式：动态地将责任附加到对象上
"""
from beverage import CoffeeA, CoffeeB
from condiment import MilkA, MilkB


def main():
    coffeea = CoffeeA()
    print(coffeea.get_desc())
    print(coffeea.get_cost())
    coffeea = MilkA(coffeea)
    print(coffeea.get_desc())
    print(coffeea.get_cost())
    coffeea = MilkA(coffeea)
    print(coffeea.get_desc())
    print(coffeea.get_cost())

    coffeeb = CoffeeB()
    print(coffeeb.get_desc())
    print(coffeeb.get_cost())
    coffeeb = MilkB(coffeeb)
    print(coffeeb.get_desc())
    print(coffeeb.get_cost())
    coffeeb = MilkB(coffeeb)
    print(coffeeb.get_desc())
    print(coffeeb.get_cost())


if __name__ == '__main__':
    main()
