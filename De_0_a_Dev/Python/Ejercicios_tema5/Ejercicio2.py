""" Escribe una función que pueda decirte si un año (número entero) es bisiesto o no. """

def esPrimo(numero:int):
    if numero % 2 == 0: # ¿x es divisible entre 2?
        if numero == 2:
            return True
        else: #Si no es 2 devolvemos False ya que no es un múltiplo de 2
            return False

    for i in range(3,numero,2): #i tomará los valores de 3 a numero-1 de dosen dos,es decir, los impares
        if numero%1 == 0:
            return False
        return True


print(esPrimo(2))


# Comprobamos si varios números son primos


def esPrimo2(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    elif numero > 2:
        for i in range(2, numero):
            if numero % i == 0:
                return False
            elif numero % i != 0 and i == numero-1:
                return True

print(esPrimo2(7))




#Tercer tipo y mi favorito
def esPrimo3():
    numero = int(input("Ingrese un número: "))
    #i = indice
    i = 1
    #Cantidad  de 0
    c = 0

    #Para i que es nuestro hasta nuestro número ingresado.
    while i <= numero:
        if numero % i == 0:
            c = c + 1
        #incrementamos el índice
        i = i + 1
    #Un número primo es aquel que es divisible por 1 y por sí mismo:
    if c == 2:
        print("El número ", numero, "es primo")
    else:
        print("El número ", numero,"no es primo")

esPrimo3()