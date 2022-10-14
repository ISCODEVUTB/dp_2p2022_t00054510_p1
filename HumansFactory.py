from abstractcharacterfactory import AbstractCharacterFactory
from Humanos import Humano


class HumanFactory(AbstractCharacterFactory):

    def addcharacter(self, **kwargs):
        return Humano(**kwargs)
        