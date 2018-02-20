from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty


class ZipIndicator(Slider):
    pass


class CircleIndicator(Widget):
    percentage = NumericProperty(0)
    max = NumericProperty(270)
    min = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
