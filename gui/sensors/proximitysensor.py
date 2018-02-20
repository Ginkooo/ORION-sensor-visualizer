from kivy.properties import NumericProperty
from kivy.clock import Clock

from gui.sensors.sensor import Sensor
from providers.proximitysensorprovider import ProximitySensorProvider
import config


class ProximitySensor(Sensor):
    """Proximity sensor view"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_provider, 0)

    def update(self, *args):
        """reffer to Sensor base class"""
        self.reading = self.provider.reading

    def set_provider(self, *args):
        """Reffer to Sensor base class"""
        self.provider = ProximitySensorProvider(self.text)
        if not config.DEBUG:
            interval = config.ProximitySensor.update_interval
            Clock.schedule_interval(self.update, interval)

    # maximum possible reading
    max = NumericProperty(config.ProximitySensor.max)
    # minimum possible reading
    min = NumericProperty(config.ProximitySensor.min)
