"""观察者

当主题信息发生变动时将推送至观察者
"""
from abc import ABCMeta, abstractmethod


class Observer(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        """更新信息
        """
        pass


class CurrentWeather(Observer):

    def __init__(self, weather_data):
        super().__init__()
        self._data = None
        weather_data.register(self)

    def update(self, data):
        self._data = data
        print("CurrentWeather: %d" % self._data)


class FutureWeather(Observer):

    def __init__(self, weather_data):
        super().__init__()
        self._data = None
        weather_data.register(self)

    def update(self, data):
        self._data = data
        print("FutureWeather: %d" % self._data)
