#!/usr/bin/env python3
from functools import partial

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.progressbar import ProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock

import config

PINK = 1, 0, 1, 1
BLACK = 0, 0, 0, 1
WHITE = 1, 1, 1, 1


class Sensor(FloatLayout):
    text = StringProperty('')
    reading = NumericProperty(20)
    color = ListProperty([1, 1, 1, 1])

    if config.DEBUG:
        def on_touch_down(self, touch):
            if self.collide_point(*touch.pos):
                self.reading += 1
                return True


class ProximitySensor(Sensor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    max = NumericProperty(1000)
    min = NumericProperty(0)


class ZipIndicator(ProgressBar):
    pass


class CircleIndicator(Widget):
    percentage = NumericProperty(0)
    max = NumericProperty(270)
    min = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Gyroscope(Sensor):
    pass


class Potentiometer(Sensor):
    pass


class SensorApp(App):
    pass


if __name__ == '__main__':
    SensorApp().run()