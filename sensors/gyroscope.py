import math

from kivy.properties import ListProperty, NumericProperty
from kivy.clock import Clock

from sensors.sensor import Sensor


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
