from abc import ABC, abstractmethod
from Personajes import Personaje

class AbstractCharacterFactory(ABC):

    @abstractmethod
    def addcharacter(self, **kwargs)-> Personaje:
        pass