import unittest


from enumerations import *

from Client import Client
from Debilidades import Debilidades
from Habilidades import Habilidades
from Personalida import Personalidad
from Poderes import Poderes
from Armas import Armas 

from Aliens import Aliens
from Artificiales import Artificiales
from Humanos import Humano
from SuperHumanos import SuperHumanos
from AliensFactory import AliensFactory
from SuperHumansFactory import SuperHumansFactory
from HumansFactory import HumanFactory
from ArtificialsFactory import ArtificialsFactory

class Testfactories(unittest.TestCase):

    dict_humano = {'name':"Juan", 'hp':100,'stamina':100,'strength': 50,'speed': 120,'armor':100,'mana': 100,'status': Estado.VIVO, 'humanStatus':HumanStatus.COMANDANTE,'sex': Sexo.HOMBRE}
    dict_alien = {'name':"Zeus",'hp': 500,'stamina': 200,'strength': 200,'speed': 30,'armor':10,'mana': 10,'status': Estado.VIVO,'RaceAlien': RazaAlienigena.NOXIANOS}
    dict_artif = {'name':'Profi', 'hp': 500,'stamina': 200,'strength': 200,'speed': 30,'armor':200, 'mana':0, 'status': Estado.VIVO, 'RangeArtificial': RangoArticial.CYBER_MECH, 'Laboratory': Laboratorio.DEXTER_LABORATORIO}
    dict_superh = {'name' :"Maria",'hp': 500,'stamina': 500,'strength': 500,'speed': 500,'armor': 500,'mana': 100,'status': Estado.VIVO,'shclass': ShClass.SUPERFUERTE}

    cliente = Client(ArtificialsFactory())

    humano_juan = cliente.buildProduct(HumanFactory(), **dict_humano)

    def test_humanfactory_instance(self):
        #self.humano_juan.Add(self.arrogancia)
        self.assertIsInstance(self.humano_juan,Humano, "Its instance!")

if __name__ == '__main__':
    unittest.main()