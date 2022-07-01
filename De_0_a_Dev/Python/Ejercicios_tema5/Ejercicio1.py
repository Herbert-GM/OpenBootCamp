""" Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo. """


def getAreaTriangulo(base, altura):
    return (base * altura)/2

def getAreaCirculo(pi, radio):
    return pi * (radio * radio)

print("==============TRIANGULO==============")
print("Calculando el área de un triángulo")
alturaTriangulo = float(input("Ingrese la altura: "))
baseTriangulo = float(input("Ingrese la base: "))

print(getAreaTriangulo(baseTriangulo,alturaTriangulo),"m2")

print("==============CIRCULO==============")

print("Calculando el área de un círculo")
radioCirculo = float(input("Ingrese el radio: "))
pi = 3.14
print(getAreaCirculo(pi,radioCirculo),"m2")