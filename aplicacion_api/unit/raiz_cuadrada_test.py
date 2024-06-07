import unittest
from app.Calculadora import Calculadora



class Raiz_Cuadrada_Tests(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()
        self.resultadoEsperado=0
        self.resultadoObtenido=0
        self.numero=0

    def test_Raiz_Cuadrada_De_Entero_Mayor_A_Cero(self):
        self.numero=9
        self.resultadoEsperado=3
        self.resultadoObtenido=self.calculadora.CalculeRaizCuadrada(self.numero)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Raiz_Cuadrada_De_Entero_Igual_A_Cero(self):
        self.numero=0
        self.resultadoEsperado=0
        self.resultadoObtenido=self.calculadora.CalculeRaizCuadrada(self.numero)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Raiz_Cuadrada_De_Entero_Menor_A_Cero(self):
        self.numero=-9
        self.resultadoEsperado=f"No existen raíces cuadradas de números negativos."

        with self.assertRaises(TypeError) as contexto:
            self.calculadora.CalculeRaizCuadrada(self.numero)

        self.assertEqual(str(contexto.exception), self.resultadoEsperado)

    def test_Parametro_No_Es_Valido(self):
        self.numero="2"
        self.resultadoEsperado=f"El parámetro {self.numero} no es de tipo numérico."

        with self.assertRaises(TypeError) as contexto:
            self.calculadora.CalculeRaizCuadrada(self.numero)

        self.assertEqual(str(contexto.exception), self.resultadoEsperado)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()        