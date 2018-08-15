"""主题

主题可以注册和移除观察者
当主题信息发生变动时，通知观察者
"""
from abc import ABCMeta, abstractmethod
from random import choice


class Subject(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def register(self, observer):
        """注册成员
        """
        pass

    @abstractmethod
    def remove(self, observer):
        """移除成员
        """
        pass

    @abstractmethod
    def notify(self):
        """将信息通知给成员
        """
        pass


class WeatherData(Subject):

    def __init__(self):
        super().__init__()
        self._observers = list()
        self._data = None

    def register(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        index = self._observers.index(observer)
        del self._observers[index]

    def change(self):
        self.set_data()
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self._data)

    def set_data(self):
        self._data = choice(range(10))
