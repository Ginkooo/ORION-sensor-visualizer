from kivy.properties import NumericProperty
from kivy.clock import Clock

from gui.sensors.sensor import Sensor
import config


class ProximitySensor(Sensor):
    """Proximity sensor view"""

    # maximum possible reading
    max = NumericProperty(config.ProximitySensor.max)
    # minimum possible reading
    min = NumericProperty(config.ProximitySensor.min)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_provider, 0)

