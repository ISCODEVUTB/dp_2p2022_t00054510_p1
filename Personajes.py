from ast import List
from abc import  abstractmethod, ABC
from Debilidades import Debilidades
from Ficha import IFicha
from enumerations import Estado
from Caracterizacion  import Caracterizacion
from Personalida import Personalidad

class Personaje(IFicha, ABC):
    __nombre: str
    __vida: float
    __estamina: float
    __mana: float
    __fuerza: float
    __velocidad: float
    __armadura: float
    __liga: str
    __enemigo: None
    __caracterizacion: List
    __estado: Estado

    def __init__(self,  nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado, caracterizacion=[], enemigo=None, liga=None):
        "Inicializador de Persojane, nombre: str, vida: float, estamina: float, fuerza: float, velocidad: float, armadura: float, caracterizacion: list of objects, enemigo: Personaje[defaul->none] liga: str"
        self.__nombre = nombre
        self.__vida = vida
        self.__mana = mana
        self.__estamina = estamina
        self.__fuerza = fuerza
        self.__velocidad = velocidad
        self.__armadura = armadura
        self.__enemigo = enemigo
        self.__liga = liga
        self.__estado = estado
        self.__caracterizacion = caracterizacion

    
    def Add(self, caracterizacion: Caracterizacion):
        self.__caracterizacion.append(caracterizacion)
    
    def getEnemigo(self):
        return self.__enemigo
    def Enemigo(self, personaje):
        self.__enemigo = personaje

    def Liga(self, liga):
        self.__liga = liga
    def getLiga(self):
        return self.__liga

    def recibirDaño(self, danio):
        """RECIBIR DAÑO """
        self.__vida -= danio
        
    def setEstado(self):
        if self.__vida <= 0:
            self.__vida = 0
            self.__estado = Estado.MUERTO
        else: 
            self.__estado = Estado.VIVO

    def getVida(self):
        return self.__vida
    
        
    def atacar(self, personaje):
        if personaje.__estado.name == "VIVO":
            personaje.recibirDaño(self.__fuerza)
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