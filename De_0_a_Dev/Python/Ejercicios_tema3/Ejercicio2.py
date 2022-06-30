"""
- Ejercicio 2 
    Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
"""

peso = input("Ingrese su peso en kilogramos: ")
estatura = input("Ingrese su estatura en metros: ")

peso = float(peso)
estatura = float(estatura)

masaCorporal = peso/(estatura * estatura)


print("Tu índice de masa corporal es:", round(masaCorporal, 2))

