from Personajes import Personaje
from Ficha import IFicha
from enumerations import RazaAlienigena

class Aliens(Personaje):
    __RaceAlien: RazaAlienigena

    def __init__(self, caracterizacion=[], enemigo=None, liga=None, **kwargs):
        super().__init__(caracterizacion, enemigo, liga, **kwargs)
        self.__RaceAlien = kwargs['RaceAlien']

    def getRazaAlien(self):
        return self.__RaceAlien.name
    