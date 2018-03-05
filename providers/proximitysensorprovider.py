from providers.provider import Provider


class ProximitySensorProvider(Provider):
    """Provides data from proximity sensors"""

    @property
    def reading(self):
        """reffer to Provider base class"""
        return 1520
