from Caracterizacion  import Caracterizacion

class Habilidades(Caracterizacion):
    __damage: float
    __cost: float

    def __init__(self, name, damage, cost):
        super().__init__(name)
        self.__damage = damage
        self.__cost = cost
    
    def getName(self):
        return self.__name
    
    def getCost(self):
        return self.__cost
    
    def getDamage(self):
        return self.__damage
        