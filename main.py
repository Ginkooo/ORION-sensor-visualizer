#!/usr/bin/env python3
from kivy.app import App

from sensors.gyroscope import Gyroscope
from sensors.potentiometer import Potentiometer
from sensors.proximitysensor import ProximitySensor
from indicators import CircleIndicator, ZipIndicator

PINK = 1, 0, 1, 1
BLACK = 0, 0, 0, 1
WHITE = 1, 1, 1, 1


class SensorApp(App):
    pass


if __name__ == '__main__':
    SensorApp().run()
