""" Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no. """

edad = input("Ingrese sue edad: ")
edad = int(edad)

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor")