from abc import ABC, abstractproperty


class Provider(ABC):
    """Base class for sensor reading providers"""

    def __init__(self, name):
        self.name = name

    @abstractproperty
    def reading(self):
        """return current sensor reading"""
        return self.provider.read()
