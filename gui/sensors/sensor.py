from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock

import config
import utils.provider
import utils.reading


class Sensor(FloatLayout):
    """Base class for sensor views"""
    # sensor name
    text = StringProperty('')
    # sensor reading (GUI)
    reading = NumericProperty(20.5)
    reading_real = NumericProperty(20.5)
    # color, it is used by some sensors
    color = ListProperty([0.3, 0.3, 0.3, 1])

    if config.DEBUG:
        def on_touch_down(self, touch):
            """for debugging, click to increase reading by some amount"""
            if self.collide_point(*touch.pos):
                try:
                    self.reading_real += 20
                except TypeError:
                    for i in range(len(self.reading)):
                        self.reading_real[i] += 100
                return True
    else:
        def on_touch_down(self, touch):
            """disables sensor widget interavtivity in non debug mode"""
            if self.collide_point(*touch.pos):
                return True
            return False

    def on_reading_real(self, instance, value):
        reading = utils.reading.normalize_value(value, self.min, self.max)
        self.reading = reading

    def update(self, *args):
        """sets GUI class 'reading_real' to actual value provided by a sensor data
        provider and 'reading' to value inside <min, max>"""
        reading_real = self.provider.reading
        self.reading_real = reading_real

    def set_provider(self, *args):
        """Uses reflection to get correct Provider class for a Sensor, then
        schedules reading update"""
        provider_cls = utils.provider.get_provider_cls(self)
        self.provider = provider_cls(self.text)
        if not config.DEBUG:
            interval = config.ProximitySensor.update_interval
            Clock.schedule_interval(self.update, interval)

