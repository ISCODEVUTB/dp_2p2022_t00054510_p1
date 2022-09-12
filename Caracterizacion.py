from abc import ABC, abstractmethod


class Caracterizacion(ABC):
    __name: str
    def __init__(self, name):
        """SOLO CREAR NOMBRE DE LA CARACTERIZACION"""
        self.__name = name
        
    
    def getName(self):
        return self.__name 
        
    
        
        
    

    
    
        