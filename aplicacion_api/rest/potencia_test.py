import http.client
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
BASE_URL = "http://localhost:5000/"
DEFAULT_TIMEOUT = 2

class Potencia_Tests(unittest.TestCase):
    def setUp(self):
        self.resultadoEsperado=None
        self.resultadoObtenido=None
        self.url=""
        self.base=0
        self.exponente=0
       
    def test_Potencia_Respuesta_Correcta(self):
        self.base=2
        self.exponente=3
        self.url=f"{BASE_URL}calcule_potencia?base={self.base}&exponente={self.exponente}"
        self.resultadoEsperado=http.client.OK
        self.resultadoObtenido=urlopen(self.url, timeout=DEFAULT_TIMEOUT).status
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Potencia_Exponente_Negativo(self):      
        try:
         self.base=2
         self.exponente=-3
         self.url=f"{BASE_URL}calcule_potencia?base={self.base}&exponente={self.exponente}"
         self.resultadoEsperado=http.client.BAD_REQUEST
         urlopen(self.url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
         self.resultadoObtenido=e.code
         self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)