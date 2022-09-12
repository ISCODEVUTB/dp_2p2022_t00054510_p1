import unittest
import enumerations

from Personalida import Personalidad
from Armas import Armas
from Poderes import Poderes
from Debilidades import Debilidades
from Habilidades import Habilidades

class TestArmas(unittest.TestCase):
    # TEST PARA ARMAS
    def test_Arma_Nombre(self):
        pistola = Armas("Pistola", 50,100,30,30)

        result1 = pistola.getName()
        self.assertEqual(result1, "Pistola")
    
    def test_Arma_Disparo(self):

        pistola = Armas("Pistola", 50,100,30,30)

        result2 = pistola.getDamage()

        self.assertEqual(result2, 50)

    # TEST PARA PODERES
    lanza_llamas = Poderes("LanzaLlamas", 500, 20, "Lanzar fuego de las manos", enumerations.Elemento.FUEGO)

    def test_poder_nombre(self):
        self.assertAlmostEqual(self.lanza_llamas.getName(), "LanzaLlamas")
    def test_poder_damage(self):
        self.assertEqual(self.lanza_llamas.getDamage(), 500)
    def test_poder_elemento(self):
        self.assertEqual(self.lanza_llamas.getElemento(), "FUEGO")

    # TEST PARA DEBILIDADES
    debilidad_veneno = Debilidades("Venenosis", enumerations.Elemento.VENENO, -0.5)

    def test_debilidad_efecto(self):
        self.assertEqual(self.debilidad_veneno.getEfecto(), -0.5)
    def test_debilidad_elemento(self):
        self.assertEqual(self.debilidad_veneno.getElemento(), "VENENO")
    # TEST PARA HABILIDADES
    lanzar_personaje = Habilidades("Lanzamiento", 500, 50)

    def test_habilidad_cost(self):
        self.assertEqual(self.lanzar_personaje.getCost(), 50)
    def test_habilidad_damage(self):
        self.assertEqual(self.lanzar_personaje.getDamage(), 500)

    # TEST PARA PERSONALIDADES 
    arrogante = Personalidad("Arrogante", "Es Arrogante JAJAJA")
    
    def test_personalidad_name(self):
        self.assertEqual(self.arrogante.getName(), "Arrogante")
    def test_personalidad_descrip(self):
        self.assertEqual(self.arrogante.getDescription(), "Es Arrogante JAJAJA")
if __name__ == "__main__":
    unittest.main()