#!/usr/bin/env python3
import math

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock

import config

PINK = 1, 0, 1, 1
BLACK = 0, 0, 0, 1
WHITE = 1, 1, 1, 1


class Sensor(FloatLayout):
    text = StringProperty('')
    reading = NumericProperty(20.5)
    color = ListProperty([0.3, 0.3, 0.3, 1])

    if config.DEBUG:
        def on_touch_down(self, touch):
            if self.collide_point(*touch.pos):
                try:
                    self.reading += 20
                except TypeError:
                    for i in range(len(self.reading)):
                        self.reading[i] += 100
                return True


class ProximitySensor(Sensor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    max = NumericProperty(1000)
    min = NumericProperty(0)


class ZipIndicator(Slider):
    pass


class CircleIndicator(Widget):
    percentage = NumericProperty(0)
    max = NumericProperty(270)
    min = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Gyroscope(Sensor):
    reading = ListProperty([0, 0, 0])
    colors = ListProperty([0, 0, 0, 1])
    line_width = NumericProperty(3.0)

    min = NumericProperty(0)
    max = NumericProperty(1000)

    points = ListProperty([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        ])

    def set_colors(self, *args):
        for i in range(3):
            self.colors[i] = self.reading[i] / self.max

    def set_points(self, *args):
        line_l = self.width / 3
        cross = ((line_l) / math.sqrt(2),
                 (line_l) / math.sqrt(2))
        self.points[0] = self.center + [self.center_x + line_l,
                                        self.center_y]
        self.points[1] = self.center + [self.center_x,
                                        self.center_y + line_l]
        self.points[2] = self.center + [self.center_x - cross[0],
                                        self.center_y - cross[1]]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_points, 1)

    def on_reading(self, *args):
        self.set_colors()


class Potentiometer(Sensor):
    pass


class SensorApp(App):
    pass


if __name__ == '__main__':
    SensorApp().run()
