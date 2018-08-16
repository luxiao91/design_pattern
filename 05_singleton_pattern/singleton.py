"""python单例模式的各种实现方式

单例模式，即在程序中始终只有一个实例
可以用于连接池、线程池、配置、注册表等
"""

# ------- SOL1：在模块中实例化，后续import实例 -------


class SingletonA(object):

    def __init__(self):
        pass

    def some_func(self):
        pass


s_a = SingletonA()

# 其他模块使用这个实例，只需要直接导入：
# from singleton import singleton_a


# ------- SOL2: __new__ -------


class SingletonB(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kw)
        return cls._instance


# ------- SOL3: 装饰器 -------

from functools import wraps


def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance


@singleton
class SingletonC(object):

    def __init__(self):
        self.data = None


# ------- SOL4: 元类 -------


class MetaSingleton(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._inst = None

    def __call__(cls, *args, **kwargs):
        if cls._inst is None:
            cls._inst = super().__call__(*args, **kwargs)
        return cls._inst


class SingletonD(metaclass=MetaSingleton):

    def __init__(self):
        self.data = None


if __name__ == "__main__":

    s_b1 = SingletonD()
    s_b1.data = 10
    print(id(s_b1))

    s_b2 = SingletonD()
    print(s_b2.data)
    print(id(s_b2))
