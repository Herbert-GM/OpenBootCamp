# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

#Importar con "import <file>" nos obligaría a utilizar <file>.<función>(n1,n2) 
from fmath import *

print("Ingrese los números a utilizar")

n1 = int(input("Ingrese el número 1: "))
n2 = int(input("Ingrese el número 2: "))

add(n1, n2)
substract(n1, n2)
multiply(n1, n2)
split(n1, n2)