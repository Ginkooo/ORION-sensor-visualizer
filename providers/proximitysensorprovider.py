from providers.provider import Provider


class ProximitySensorProvider(Provider):

    def __init__(self, name):
        self.name = name

    @property
    def reading(self):
        return 42
