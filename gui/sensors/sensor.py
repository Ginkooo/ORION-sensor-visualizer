import importlib

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock

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

    def update(self, *args):
        """sets GUI class 'reading' to actual value provided by a sensor data
        provider"""
        self.reading = self.provider.reading

    def set_provider(self, *args):
        """Uses reflection to get correct Provider class for a Sensor, then
        schedules reading update"""
        provider_cls_name = self.__class__.__name__ + 'Provider'
        provider_module_name = provider_cls_name.lower()
        provider_module_path = (config.PROVIDERS_PACKAGE + '.' +
                                provider_module_name)
        try:
            module = importlib.import_module(provider_module_path)
        except ImportError:
            raise ImportError('Couldnt import module, please reffer to'
                              'documentation on "How to add sensors"')
        provider_cls = getattr(module, provider_cls_name)
        self.provider = provider_cls(self.text)
        if not config.DEBUG:
            interval = config.ProximitySensor.update_interval
            Clock.schedule_interval(self.update, interval)
