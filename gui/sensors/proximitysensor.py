from kivy.properties import NumericProperty

from gui.sensors.sensor import Sensor
import config


class ProximitySensor(Sensor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    max = NumericProperty(config.ProximitySensor.max)
    min = NumericProperty(config.ProximitySensor.min)


