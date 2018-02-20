from providers.provider import Provider


class ProximitySensorProvider(Provider):
    """Provides data from proximity sensors"""

    def __init__(self, name):
        # proximity sensor name (for differencing sensors)
        self.name = name

    @property
    def reading(self):
        """reffer to Provider base class"""
        return 42
