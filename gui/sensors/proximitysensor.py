from kivy.properties import NumericProperty

from gui.sensors.sensor import Sensor


class ProximitySensor(Sensor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    max = NumericProperty(1000)
    min = NumericProperty(0)


