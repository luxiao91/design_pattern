"""装饰者模式：动态地将责任附加到对象上

其实可以直接用装饰器，也是python更好用的方法
然而懒得写了，就这么着吧
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
