from Personajes import Personaje
from enumerations import ShClass

class SuperHumanos(Personaje):
    __ShClases: ShClass

    def __init__(self,  nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado, clase, caracterizacion=[], enemigo=None, liga=None):
        super().__init__(nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado, caracterizacion, enemigo, liga)
        self.__ShClases = clase

    def getShClases(self):
        return self.__ShClases.name