# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

# Importamos el módulo time para poder coger la hora.
import time

# Inicializamos las variables y formateamos el tiempo para que solo se vean las horas y minutos
""" i. strftime()
Now what if you wanted to display the Python date and time in the format you wish to? The strftime() method takes a format and optionally, a Python time tuple, and returns the date in the format you specify. The syntax is as follows.
Time.strftime(format[, t]) """

hora = time.strftime('%H') # %H – hour; using a 24-hr clock (0 to 23)
minutos = time.strftime('%M') # %M – minute

# Comprobamos si la hora es mayor o igual a 19. Si es mayor, mostrará un mensaje y en el caso de que sea menor mostrará un mensaje informando de las horas y minutos que faltan para ir a casa.
if int(hora) >= 19:
	print ("Es hora de irse a casa") 
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))
