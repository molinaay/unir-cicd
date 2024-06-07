import http.client
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
BASE_URL = "http://localhost:5000/"
DEFAULT_TIMEOUT = 2

class Logaritmo_Base_10_Tests(unittest.TestCase):
    def setUp(self):
        self.resultadoEsperado=None
        self.resultadoObtenido=None
        self.url=""
        self.numero=0
       
    def test_Logaritmo_Base_10_Correcto(self):
        self.numero=6
        self.url=f"{BASE_URL}calcule_logaritmo_base_10?numero={self.numero}"
        self.resultadoEsperado=http.client.OK
        self.resultadoObtenido=urlopen(self.url, timeout=DEFAULT_TIMEOUT).status
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Logaritmo_Base_10_Numero_Negativo(self):      
        try:
         self.numero=-6
         self.url=f"{BASE_URL}calcule_logaritmo_base_10?numero={self.numero}"
         self.resultadoEsperado=http.client.BAD_REQUEST
         urlopen(self.url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
         self.resultadoObtenido=e.code
         self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)
