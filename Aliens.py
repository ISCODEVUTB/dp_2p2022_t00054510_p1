from Personajes import Personaje
from Ficha import IFicha
from enumerations import RazaAlienigena

class Aliens(Personaje):
    __RazaAlienigena: RazaAlienigena

    def __init__(self,  nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado,RazaAlien, caracterizacion=[], enemigo=None, liga=None):
        super().__init__(nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado, caracterizacion, enemigo, liga)
        self.__RazaAlienigena = RazaAlien

    def getRazaAlien(self):
        return self.__RazaAlienigena.name
    