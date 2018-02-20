from kivy.properties import NumericProperty

from gui.sensors.sensor import Sensor
import config


class Potentiometer(Sensor):
    """Potentiometer sensor view"""
    max = NumericProperty(config.Potentiometer.max)
    min = NumericProperty(config.Potentiometer.min)
