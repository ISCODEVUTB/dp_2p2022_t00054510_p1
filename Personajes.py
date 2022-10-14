from ast import List
from abc import  abstractmethod, ABC
from Debilidades import Debilidades
from Ficha import IFicha
from enumerations import Estado
from Caracterizacion  import Caracterizacion
from Personalida import Personalidad

class Personaje(IFicha, ABC):
    __name: str
    __hp: float
    __stamina: float
    __mana: float
    __strength: float
    __speed: float
    __armor: float
    __ligue: str
    __enemy: None
    __caracterizacion: List
    __status: Estado

    def __init__(self, caracterizacion=[], enemy=None, ligue=None,**kwargs):
        "Inicializador de Persojane, nombre: str, vida: float, estamina: float, fuerza: float, velocidad: float, armadura: float, caracterizacion: list of objects, enemigo: Personaje[defaul->none] liga: str"
        
        self.__name = kwargs['name']
        self.__hp = kwargs['hp']
        self.__mana = kwargs['mana']
        self.__stamina = kwargs['stamina']
        self.__strength = kwargs['strength']
        self.__speed = kwargs['speed']
        self.__armor = kwargs['armor']
        self.__enemy = enemy
        self.__ligue = ligue
        self.__status = kwargs['status']
        self.__caracterizacion = caracterizacion

    
    def Add(self, caracterizacion: Caracterizacion):
        self.__caracterizacion.append(caracterizacion)
    
    def getEnemigo(self):
        return self.__enemy
    def Enemigo(self, personaje):
        self.__enemy = personaje

    def Liga(self, ligue):
        self.__ligue = ligue
    def getLiga(self):
        return self.__ligue

    def recibirDaño(self, danio):
        """RECIBIR DAÑO """
        self.__hp -= danio
        
    def setEstado(self):
        if self.__hp <= 0:
            self.__hp = 0
            self.__status = Estado.MUERTO
        else: 
            self.__status = Estado.VIVO

    def getVida(self):
        return self.__hp
    
        
    def atacar(self, personaje):
        if personaje.__estado.name == "VIVO":
            personaje.recibirDaño(self.__strength)
            print("Ataque basico ha sido exitoso")
        else: 
            print("Personaje no esta vivo. . . .")

    def ataqueEspecial(self, personaje, ataqueEspecial):
        if personaje.__estado.name == "VIVO":

            for ataque in super().__caracterizacion:
                if ataque.getName() == ataqueEspecial:
                    if isinstance(ataque, Personalidad) or isinstance(ataque, Debilidades):
                        print("no se puede atacar con una Personalidad")
                    else:
                        personaje.recibirDaño(ataque.getDamage())
                        print("Has atacado con exito. . .")
        else: 
            print("Personaje muerto")


    def add_test(self, existencia: Caracterizacion):
        for i in self.__caracterizacion:
            if i == existencia:
                return True
            else:
                False