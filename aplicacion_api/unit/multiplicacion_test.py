import unittest
from app.Calculadora import Calculadora



class Multiplicacion_Tests(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()
        self.resultadoEsperado=0
        self.resultadoObtenido=0
        self.primerNumero=0
        self.segundoNumero=0

    def test_Multiplicacion_Con_Dos_Numeros_Positivos_Resultado(self):
        self.primerNumero=5
        self.segundoNumero=3
        self.resultadoEsperado=15
        self.resultadoObtenido=self.calculadora.Multiplique(self.primerNumero,
                                                     self.segundoNumero)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Multiplicacion_Con_Dos_Numeros_Negativos_Resultado(self):
        self.primerNumero=-2
        self.segundoNumero=-3
        self.resultadoEsperado=6
        self.resultadoObtenido=self.calculadora.Multiplique(self.primerNumero,
                                                     self.segundoNumero)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Multiplicacion_Con_Numero_Positivo_Y_Negativo_Resultado(self):
        self.primerNumero=2
        self.segundoNumero=-3
        self.resultadoEsperado=-6
        self.resultadoObtenido=self.calculadora.Multiplique(self.primerNumero,
                                                     self.segundoNumero)
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Parametro_No_Es_Valido(self):
        self.primerNumero="2"
        self.segundoNumero=-3
        self.resultadoEsperado=f"El parámetro {self.primerNumero} no es de tipo numérico."

        with self.assertRaises(TypeError) as contexto:
            self.calculadora.Multiplique(self.primerNumero, self.segundoNumero)

        self.assertEqual(str(contexto.exception), self.resultadoEsperado)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()        