from kivy.properties import NumericProperty
from kivy.clock import Clock

from gui.sensors.sensor import Sensor
from providers.proximitysensorprovider import ProximitySensorProvider
import config


class ProximitySensor(Sensor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_provider, 0)

    def update(self, *args):
        self.reading = self.provider.reading

    def set_provider(self, *args):
        self.provider = ProximitySensorProvider(self.text)
        if not config.DEBUG:
            interval = config.ProximitySensor.update_interval
            Clock.schedule_interval(self.update, interval)

    max = NumericProperty(config.ProximitySensor.max)
    min = NumericProperty(config.ProximitySensor.min)
