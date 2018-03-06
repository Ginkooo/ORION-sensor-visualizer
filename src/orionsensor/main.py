#!/usr/bin/env python3
from kivy.app import App

from gui.sensors.gyroscope import Gyroscope
from gui.sensors.potentiometer import Potentiometer
from gui.sensors.proximitysensor import ProximitySensor
from gui.indicators import CircleIndicator, ZipIndicator

PINK = 1, 0, 1, 1
BLACK = 0, 0, 0, 1
WHITE = 1, 1, 1, 1


class SensorApp(App):
    pass


if __name__ == '__main__':
    SensorApp().run()
