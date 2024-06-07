import math
class Calculadora:

    def ValideQueSeaNumerico(self, numero):
        if not isinstance(numero, (int, float)):
            raise TypeError(f"El parámetro {numero} no es de tipo numérico.")

    
    def Sume(self, primerNumero, segundoNumero):
        self.ValideQueSeaNumerico(primerNumero)
        self.ValideQueSeaNumerico(segundoNumero)
        return primerNumero + segundoNumero
    
    def Reste(self, primerNumero, segundoNumero):
        self.ValideQueSeaNumerico(primerNumero)
        self.ValideQueSeaNumerico(segundoNumero)
        return primerNumero - segundoNumero
    
    def Multiplique(self, primerNumero, segundoNumero):
        self.ValideQueSeaNumerico(primerNumero)
        self.ValideQueSeaNumerico(segundoNumero)
        return primerNumero * segundoNumero
    
    def Divida(self, primerNumero, segundoNumero):
        self.ValideQueSeaNumerico(primerNumero)
        self.ValideQueSeaNumerico(segundoNumero)
        if segundoNumero != 0:
            return primerNumero / segundoNumero
        else:
            raise TypeError("No se puede dividir por 0.")
        
    def CalculePotencia(self, base, exponente):
         self.ValideQueSeaNumerico(base)
         self.ValideQueSeaNumerico(exponente)
         return base ** exponente
    
    def CalculeRaizCuadrada(self, numero):
        self.ValideQueSeaNumerico(numero)
        if numero>=0:
         return math.sqrt(numero)
        else:
         raise TypeError("No existen raíces cuadradas de números negativos.")
    
    def CalculeLogaritmoEnBase10(self,numero):
         self.ValideQueSeaNumerico(numero)
         if numero>0:
          return math.log10(numero)
         elif numero == 0:
          raise TypeError("No existe el logaritmo de cero.") 
         else:     
          raise TypeError("Los números negativos no tienen logaritmo.") 