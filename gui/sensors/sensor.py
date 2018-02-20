from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty

import config


class Sensor(FloatLayout):
    """Base class for sensor views"""
    # sensor name
    text = StringProperty('')
    # sensor reading (GUI)
    reading = NumericProperty(20.5)
    # color, it is used by some sensors
    color = ListProperty([0.3, 0.3, 0.3, 1])

    if config.DEBUG:
        def on_touch_down(self, touch):
            """for debugging, click to increase reading by some amount"""
            if self.collide_point(*touch.pos):
                try:
                    self.reading += 20
                except TypeError:
                    for i in range(len(self.reading)):
                        self.reading[i] += 100
                return True

    def update(self):
        """sets GUI class 'reading' to actual value provided by a sensor data
        provider"""
        self.reading = self.provider.reading
