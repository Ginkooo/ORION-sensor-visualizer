from abc import ABC, abstractproperty


class Provider(ABC):
    """Base class for sensor reading providers"""

    @abstractproperty
    def reading(self):
        """return current sensor reading"""
        return self.provider.read()
