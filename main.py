#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty

PINK = 1, 0, 1, 1
BLACK = 0, 0, 0, 1
WHITE = 1, 1, 1, 1


class Sensor(FloatLayout):
    text = StringProperty('')
    reading = NumericProperty(5)


class ProximitySensor(Sensor):
    max = NumericProperty(10)
    min = NumericProperty(0)


class ZipIndicator(ProgressBar):
    pass


class Gyroscope(Sensor):
    pass


class Potentiometer(Sensor):
    pass


class SensorApp(App):
    pass


if __name__ == '__main__':
    SensorApp().run()
