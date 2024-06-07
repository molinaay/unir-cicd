import unittest
from app.Calculadora import Calculadora



class Potencia_Tests(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()
        self.resultadoEsperado=0
        self.resultadoObtenido=0
        self.base=0
        self.exponente=0

    def test_Potencia_Con_Dos_Base_Positiva_Y_Exponente_Positivo_Resultado(self):
        self.base=6
        self.exponente=3
        self.resultadoEsperado=216
        self.resultadoObtenido=self.calculadora.CalculePotencia(self.base,
                                                     self.exponente)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Potencia_Con_Dos_Base_Negativa_Y_Exponente_Negativo_Resultado(self):
        self.base=-2
        self.exponente=-3
        self.resultadoEsperado=-0.125
        self.resultadoObtenido=self.calculadora.CalculePotencia(self.base,
                                                     self.exponente)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Potencia_Con_Dos_Base_Negativa_Y_Exponente_Positivo_Resultado(self):
        self.base=-2
        self.exponente=3
        self.resultadoEsperado=-8
        self.resultadoObtenido=self.calculadora.CalculePotencia(self.base,
                                                     self.exponente)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Potencia_Con_Dos_Base_Positiva_Y_Exponente_Negativo_Resultado(self):
        self.base=2
        self.exponente=-3
        self.resultadoEsperado=0.125
        self.resultadoObtenido=self.calculadora.CalculePotencia(self.base,
                                                     self.exponente)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)


    def test_Parametro_No_Es_Valido(self):
        self.base="2"
        self.exponente=-3
        self.resultadoEsperado=f"El parámetro {self.base} no es de tipo numérico."

        with self.assertRaises(TypeError) as contexto:
            self.calculadora.CalculePotencia(self.base, self.exponente)

        self.assertEqual(str(contexto.exception), self.resultadoEsperado)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()        