from Personajes import Personaje
from enumerations import HumanStatus, Sexo

class Humano(Personaje):
    __HumanStatus: HumanStatus
    __Sexo: Sexo

    def __init__(self,  nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado, HumanStatus, sexo, caracterizacion=[], enemigo=None, liga=None):
        "Instanciar un humano para agregarlo al juego, puedes agregarle caracteristicas"
        super().__init__(nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado, caracterizacion, enemigo, liga)
        self.__HumanStatus = HumanStatus
        self.__Sexo = sexo

    def getHumanStatus(self):
        return self.__HumanStatus.name
    def getSexo(self):
        return self.__Sexo.name