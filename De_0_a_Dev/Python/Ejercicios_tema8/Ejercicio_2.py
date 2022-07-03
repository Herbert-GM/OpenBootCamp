#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.


""" The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”. """
from pickle import *

class Vehiculo:
    #The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach.
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    #The __str__ method in Python represents the class objects as a string 
    def __str__(self):
        return f"Mi Color es: {self.color}, y tengo {self.puertas} puertas"


# Instanciación del objeto con parámetros
corsa = Vehiculo("Azul", "4")
# Llamado a la clase Vehiculo
print(corsa)

# Creación del archivo binario con w+b (lectura y escritura binaria)
file = open('vehiculo_objeto', 'w+b')

#pickle.dump(Clase, <archivo>)
dump(corsa, file)

# Regresamos el punto a la posición 0
file.seek(0)

# Cargamos la clase Vehiculo a través del <archivo> file
 
"""
Ejemplo del video:
f = open('<nombreDelArchivo>', 'rb')
potato = pickle.load(f)
f.close()

"""
nuevo_corsa = load(file)

print(nuevo_corsa)
file.close()