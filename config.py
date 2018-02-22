class ProximitySensor():
    # minimum value, which sensor provides
    min = 0
    # maximum
    max = 1000
    # unit, in which measurement is done
    unit = 'cm'
    # GUI updating interval (updating with actual reading)
    update_interval = 1/20


class Gyroscope():
    min = 0
    max = 1000
    unit = 'rad/sek^2'
    update_interval = 1/20


class Potentiometer():
    min = 0
    max = 270
    unit = 'degrees'
    update_interval = 1/20


PROVIDERS_PACKAGE = 'providers'


DEBUG = False
