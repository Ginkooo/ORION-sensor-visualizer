import math

from kivy.properties import ListProperty, NumericProperty
from kivy.clock import Clock

from gui.sensors.sensor import Sensor
import config


class Gyroscope(Sensor):
    """Gyroscope sensor view"""
    reading = ListProperty([0, 0, 0])
    colors = ListProperty([0, 0, 0, 1])
    line_width = NumericProperty(3.0)

    min = NumericProperty(config.Gyroscope.min)
    max = NumericProperty(config.Gyroscope.max)

    points = ListProperty([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        ])

    def set_colors(self, *args):
        """sets colors to visually represent readings"""
        for i in range(3):
            self.colors[i] = self.reading[i] / self.max

    def set_points(self, *args):
        """set up lines for reading indicators"""
        line_l = self.height / 3
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
        """set colors on reading change"""
        self.set_colors()

    def on_size(self, *args):
        """resise graph on sensor view resize"""
        self.set_points()
