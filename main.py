from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty


class Sensor(FloatLayout):
    text = StringProperty('')
    reading = NumericProperty(0)


class ProximitySensor(Sensor):
    percentage = NumericProperty(0.5)


class Gyroscope(Sensor):
    pass


class Potentiometer(Sensor):
    pass


class SensorApp(App):
    pass


if __name__ == '__main__':
    SensorApp().run()
