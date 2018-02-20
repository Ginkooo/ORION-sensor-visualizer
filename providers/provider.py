from abc import ABC, abstractproperty


class Provider(ABC):

    @abstractproperty
    def reading(self):
        return self.provider.read()
