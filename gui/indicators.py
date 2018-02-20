from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock


class ZipIndicator(Slider):
    """Just a slider child class, for displaying one-axis reading"""
    pass


class CircleIndicator(Widget):
    """Display one-axis reading, but looks like an non-complete ring"""
    percentage = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_properties, 0)

    def set_properties(self, *args):
        self.max = self.parent.max
        self.min = self.parent.min
