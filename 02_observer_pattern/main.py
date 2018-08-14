"""观察者模式

定义对象之间的一对多依赖
当一个对象（subject）改变状态时，它的所有依赖者（observer）
都会收到通知并更新
"""
from subject import WeatherData
from observer import CurrentWeather, FutureWeather


def main():
    weather_data = WeatherData()
    current = CurrentWeather(weather_data)
    future = FutureWeather(weather_data)

    weather_data.change()
    weather_data.change()


if __name__ == '__main__':
    main()
