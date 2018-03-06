from providers.provider import Provider


class PotentiometerProvider(Provider):
    """Provide data for potentiometer view"""

    @property
    def reading(self):
        """override parent property"""
        return 42
