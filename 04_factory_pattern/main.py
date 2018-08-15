"""工厂模式

工厂方法模式：store
定义了一个创建对象的接口
由子类决定要实例化是类是哪一个

抽象工厂模式：ingredient
提供一个接口，用于创建相关或依赖对象的加组
不需要明确指定具体类
"""
from store import NYPizzaStore, CHPizzaStore


def main():
    ny_store = NYPizzaStore()
    ny_store.order_pizza("cheese")

    ch_store = CHPizzaStore()
    ch_store.order_pizza("clam")


if __name__ == '__main__':
    main()
