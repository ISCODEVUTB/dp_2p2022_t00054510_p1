from Caracterizacion  import Caracterizacion

class Personalidad(Caracterizacion):
    __description: str
    def __init__(self, nombre, description):
        super().__init__(nombre)
        self.__description = description

    def getDescription(self):
        return self.__description