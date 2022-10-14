import unittest


from enumerations import *

from Debilidades import Debilidades
from Habilidades import Habilidades
from Personalida import Personalidad
from Poderes import Poderes
from Armas import Armas 

from Aliens import Aliens
from Artificiales import Artificiales
from Humanos import Humano
from SuperHumanos import SuperHumanos

class TestPersonaje(unittest.TestCase):
    
    # PERSONAJES PARA TESTEAR
    dict_humano = {'name':"Juan", 'hp':100,'stamina':100,'strength': 50,'speed': 120,'armor':100,'mana': 100,'status': Estado.VIVO, 'humanStatus':HumanStatus.COMANDANTE,'sex': Sexo.HOMBRE}
    dict_alien = {'name':"Zeus",'hp': 500,'stamina': 200,'strength': 200,'speed': 30,'armor':10,'mana': 10,'status': Estado.VIVO,'RaceAlien': RazaAlienigena.NOXIANOS}
    dict_artif = {'name':'Profi', 'hp': 500,'stamina': 200,'strength': 200,'speed': 30,'armor':200, 'mana':0, 'status': Estado.VIVO, 'RangeArtificial': RangoArticial.CYBER_MECH, 'Laboratory': Laboratorio.DEXTER_LABORATORIO}
    dict_superh = {'name' :"Maria",'hp': 500,'stamina': 500,'strength': 500,'speed': 500,'armor': 500,'mana': 100,'status': Estado.VIVO,'shclass': ShClass.SUPERFUERTE}
    alien_zeus = Aliens(**dict_alien)
    humano_juan = Humano(**dict_humano)
    Artificial_profi = Artificiales(**dict_artif)
    super_humano_maria = SuperHumanos(**dict_superh)
    


    # Caracterizacion para Testear

    pistola = Armas("Pistola", 50,100,30,30)
    m14 = Armas("M14", 70,100,30,30)

    lanza_llamas = Poderes("LanzaLlamas", 500, 100, "LanzaLlamas", Elemento.FUEGO)
    
    pirophobia = Debilidades("Pirophofia", Elemento.FUEGO, -0.4)
    venenophobia = Debilidades("venenophiba", Elemento.VENENO, -0.4)
    
    arrogancia = Personalidad("Arrogancia", "Es Arrogante")
    astucia = Personalidad("Astucia", "Es Astucia")

    lanzar_piedrotas = Habilidades("Lanzar Piedrotas", 500, 20)

    # TESTEAR METODO ADD 
    def test_personaje_add(self):
        self.humano_juan.Add(self.arrogancia)
        self.assertTrue(self.humano_juan.add_test(self.arrogancia))
    
    # TESTEAR METODO ENEMIGO
    def test_personaje_Enemigo(self):
        self.humano_juan.Enemigo(self.alien_zeus)
        self.assertEqual(self.humano_juan.getEnemigo(), self.alien_zeus)
    # TESTEAR SETEO DE LIGA 

    def test_personaje_liga(self):
        self.humano_juan.Liga("Exmachines")
        self.assertEqual(self.humano_juan.getLiga(), "Exmachines")


if __name__ == "__main__":
    unittest.main()