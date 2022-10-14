from Personajes import Personaje
from enumerations import ShClass

class SuperHumanos(Personaje):
    __ShClases: ShClass

    def __init__(self, caracterizacion=[], enemy=None, ligue=None, **kwargs):
        super().__init__(caracterizacion, enemy, ligue, **kwargs)
        self.__ShClases = kwargs['shclass']

    def getShClases(self):
        return self.__ShClases.name