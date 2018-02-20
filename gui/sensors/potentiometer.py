from kivy.properties import NumericProperty

from gui.sensors.sensor import Sensor
import config


class Potentiometer(Sensor):
    max = NumericProperty(config.Potentiometer.max)
    min = NumericProperty(config.Potentiometer.min)
