import http.client
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
BASE_URL = "http://localhost:5000/"
DEFAULT_TIMEOUT = 2

class Multiplicacion_Tests(unittest.TestCase):
    def setUp(self):
        self.resultadoEsperado=None
        self.resultadoObtenido=None
        self.url=""
        self.primerNumero=0
        self.segundoNumero=0
       
    def test_Multiplicacion_Respuesta_Correcta(self):
        self.primerNumero=6
        self.segundoNumero=3
        self.url=f"{BASE_URL}multiplique?primerNumero={self.primerNumero}&segundoNumero={self.segundoNumero}"
        self.resultadoEsperado=http.client.OK
        self.resultadoObtenido=urlopen(self.url, timeout=DEFAULT_TIMEOUT).status
        self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

    def test_Multiplicacion_Parametro_Incorrecto(self):      
        try:
         self.primerNumero=6
         self.segundoNumero="z"
         self.url=f"{BASE_URL}multiplique?primerNumero={self.primerNumero}&segundoNumero={self.segundoNumero}"
         self.resultadoEsperado=http.client.BAD_REQUEST
         urlopen(self.url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
         self.resultadoObtenido=e.code
         self.assertEqual(self.resultadoEsperado,self.resultadoObtenido)

