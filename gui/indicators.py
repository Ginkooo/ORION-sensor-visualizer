from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock


class ZipIndicator(Slider):
    pass


class CircleIndicator(Widget):
    percentage = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_properties, 0)

    def set_properties(self, *args):
        self.max = self.parent.max
        self.min = self.parent.min
