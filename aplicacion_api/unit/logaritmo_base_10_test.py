import unittest
from app.Calculadora import Calculadora



class Logaritmo_Base_10_Tests(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()
        self.resultadoEsperado=0
        self.resultadoObtenido=0
        self.numero=0

    def test_Logaritmo_Base_10_De_Entero_Mayor_A_Cero(self):
        self.numero=2
        self.resultadoEsperado=0.3010299956639812
        self.resultadoObtenido=self.calculadora.CalculeLogaritmoEnBase10(self.numero)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Logaritmo_Base_10_De_Entero_Igual_A_Cero(self):
        self.numero=0
        self.resultadoEsperado=f"No existe el logaritmo de cero."

        with self.assertRaises(TypeError) as contexto:
            self.calculadora.CalculeLogaritmoEnBase10(self.numero)

        self.assertEqual(str(contexto.exception), self.resultadoEsperado)

    def test_Logaritmo_Base_10_De_Entero_Menor_A_Cero(self):
        self.numero=-9
        self.resultadoEsperado=f"Los números negativos no tienen logaritmo."

        with self.assertRaises(TypeError) as contexto:
            self.calculadora.CalculeLogaritmoEnBase10(self.numero)

        self.assertEqual(str(contexto.exception), self.resultadoEsperado)

    def test_Parametro_No_Es_Valido(self):
        self.numero="2"
        self.resultadoEsperado=f"El parámetro {self.numero} no es de tipo numérico."

        with self.assertRaises(TypeError) as contexto:
            self.calculadora.CalculeLogaritmoEnBase10(self.numero)

        self.assertEqual(str(contexto.exception), self.resultadoEsperado)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()        