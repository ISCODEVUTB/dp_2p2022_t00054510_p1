from abstractcharacterfactory import AbstractCharacterFactory
from Artificiales import Artificiales

class ArtificialsFactory(AbstractCharacterFactory):

    def addcharacter(self, **kwargs):
        return Artificiales(**kwargs)