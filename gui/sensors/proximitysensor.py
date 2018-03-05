from kivy.properties import NumericProperty

from gui.sensors.sensor import Sensor
import config


class ProximitySensor(Sensor):
    """Proximity sensor view"""

    # maximum possible reading
    max = NumericProperty(config.ProximitySensor.max)
    # minimum possible reading
    min = NumericProperty(config.ProximitySensor.min)
