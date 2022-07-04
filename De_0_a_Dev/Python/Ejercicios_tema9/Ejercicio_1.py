#Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

# Se pide "," para  tener un punto de separación con el que luego se dividirán el texto
items = input("Introduce países separados por comas:\n")

# FOR para recorrer y separar las palabras utilizamos el método .split("<caracterDeControl>"), generando y guardando la lista 
paises = [pais for pais in items.split(",")]
#paises = items.split(",")

# Se imprime como lista
print(paises)

# Sets: son colecciones desordenadas de objetos únicos. No se repiten
# canasta = {"manzana", "platano", "pera", "manzana", "naranja", "pera"}
# imprime {"naranja", "platano", "manzana", "pera"}
# https://www.youtube.com/watch?v=GdUwYO4Ru_s


# sorted ordena en base al código ASCI
# <caracter>.join() The join() method takes all items in an iterable and joins them into one string.
print(",".join(sorted(list(set(paises)))))