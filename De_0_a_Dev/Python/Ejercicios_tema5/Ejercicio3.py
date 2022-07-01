""" Escribe una función que pueda decirte si un año (número entero) es bisiesto o no. """

#REGLAS:
"""
1. Si es divisible por 4, es bisiesto
2. Si es divisible por 100, no es bisiesto,
salvo si es divisible  por 400, entonces es bisiesto
"""


def leap_year():
    year = int(input("Ingrese el año que desea verificar: "))

    R1 = False
    R2 = False

    if year % 4 == 0:
        R1 = True
    
    
    if year % 100 != 0 or year % 400 == 0:
        R2 = True
    

    if R1 is True and R2 is True:
        print(f"El añor {year} SÍ es Bisiesto")
    else:
        print(f"El año {year} NO es Bisiesto")


leap_year()



