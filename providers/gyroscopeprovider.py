from providers.provider import Provider


class GyroscopeProvider(Provider):
    """Provide data for gyroscope"""

    @property
    def reading(self):
        """override base method"""
        return [42, 42, 42]
