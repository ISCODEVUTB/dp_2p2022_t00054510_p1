from abc import ABC, abstractmethod
from Caracterizacion import Caracterizacion



class IFicha(ABC):

    @abstractmethod
    def Add(self, caracterizacion: Caracterizacion):
        "caracterizacion: Tipo de caracterizacion[PODERES, HABILIDADES, DEBILIDADES, PERSONALIDAD]"
    
        pass
    @abstractmethod
    def Liga(self, liga):
        """ ELEGIR LIGA A LA QUE PERTENECE EL PERSONAJE 
            
            input:
                liga: string
            output:
                return -> None
        """
        pass
    @abstractmethod
    def Enemigo(self, enemigo):
        """Elegir Enemigo del personaje creado
            
            input:
                enemigo: Personaje
            output:
                return -> None
        """
        pass
    
