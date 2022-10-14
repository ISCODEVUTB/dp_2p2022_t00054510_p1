from abstractcharacterfactory import AbstractCharacterFactory
from Aliens import Aliens


class AliensFactory(AbstractCharacterFactory):

    def addcharacter(self, **kwargs):
        return Aliens(**kwargs)