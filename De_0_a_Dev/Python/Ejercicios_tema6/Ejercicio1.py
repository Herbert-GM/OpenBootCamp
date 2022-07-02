""" - Ejercicio 1 

    En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

    * Color
    * Ruedas
    * Puertas

    Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

    * Velocidad
    * Cilindrada

    Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""


# Inicializamos la clase
class Vehiculo():
    # inicializamos los atributos
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def Informacion(self):
        print("Color:",self.color)
        print("Ruedas:",self.ruedas)
        print("Puertas:",self.puertas)
    #def __str__(self) -> str:
        #return f"Color {self.color}, ruedas {self.ruedas}"
        #return "Color {}, {} ruedas".format(self.color, self.ruedas, self.puertas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def Informacion(self):
        print("Color:",self.color)
        print("Ruedas:",self.ruedas)
        print("Puertas:",self.puertas)
        print("Velocidad:",self.velocidad,"km/h")
        print("Cilindrada:",self.puertas, "cc")
    
    #def __str__(self) -> str:
        #return f"color {self.color}, ruedas{self.ruedas}, puertas{self.puertas}, {self.velocidad} km/h, {self.cilindrada}cc"
        #return "color {}, {} km/h, {} ruedas, {} puertas, {} cilindrada".format(self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada)




coche = Coche("Azul", 4, 4, 150, 1200)
moto = Vehiculo("Rojo", 2, 0)

coche.Informacion()
print("=================================")
moto.Informacion()