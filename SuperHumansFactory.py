from abstractcharacterfactory import AbstractCharacterFactory
from SuperHumanos import SuperHumanos

class SuperHumansFactory(AbstractCharacterFactory):

    def addcharacter(self, **kwargs):
        return SuperHumanos(**kwargs)