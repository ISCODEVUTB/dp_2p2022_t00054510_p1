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
    humano_juan = Humano("Juan", 100, 100, 50, 120, 100, 100, Estado.VIVO, HumanStatus.COMANDANTE, Sexo.HOMBRE)
    alien_zeus = Aliens("Zeus", 500, 200, 200, 30, 10, 10, Estado.VIVO, RazaAlienigena.NOXIANOS)
    Artificial_profi = Artificiales("Profi", 800, 150, 300, 70, 200, RangoArticial.CYBER_MECH, Laboratorio.DEXTER_LABORATORIO)
    super_humano_maria = SuperHumanos("Maria", 500, 500, 500,500,500, 100, Estado.VIVO,ShClass.SUPERFUERTE)


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