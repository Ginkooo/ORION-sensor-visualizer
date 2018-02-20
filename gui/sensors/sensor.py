from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty

import config


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

    def update(self):
        self.reading = self.provider.reading
