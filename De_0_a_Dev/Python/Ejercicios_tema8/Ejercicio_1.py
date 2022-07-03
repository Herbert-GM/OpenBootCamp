#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

#Crear archivo - Se crea en la carpeta principal en el Visual Studio Code
archivo_texto=open("archivo.txt","w")

#Ingresamos información
archivo_texto.write("Bienvenido! a tu archivo creado\n")

# Para que se guarde lo ingresado con .write se debe cerrar
archivo_texto.close()

# El modo r+ se utiliza para abrir un archivo tanto para lectura como para escritura. Al igual que en el modo anterior, el puntero de archivo en este modo también se coloca en el punto de inicio del archivo.
archivo_texto = open("archivo.txt", "r+")

# Read the first line of the file "demofile.txt":
archivo_texto.readline()

archivo_texto.write('Esta es la segunda vez que escribo.\n')

# Cuando se creó el archivo se crea también un puntero que se coloca al comienzo del archivo, cuando lo leemos por primera vez con el readline() ese puntero se queda en al final del archivo, como agregamos un texto después tenemos que devolver el puntero al inicio del archivo, para que muestre todo desde un inicio
archivo_texto.seek(0)
print(archivo_texto.read())
archivo_texto.close()