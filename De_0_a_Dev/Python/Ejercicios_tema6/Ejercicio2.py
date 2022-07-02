""" En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. """

# inicializamos la clase
class Alumno:
    # inicializamos los atributos
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
 
    # función para imprimir los datos
    def imprimir(self):
               print("Nombre:",self.nombre)
               print("Nota:",self.nota)
 
 
    # función para obtener el resultado
    def resultado(self):
            if self.nota < 5:
                print("El alumno ha suspendido")
            else:
                print("El alumno ha aprobado")
 
 
 
# bloque principal
# creamos los nuevos objetos
alumno1=Alumno()
alumno2=Alumno()
 
# inicializamos los atributos
alumno1.inicializar("María",8)
alumno2.inicializar("Pepe",4)
 
# imprimimos los datos y resultados de cada alumno
print("================ALUMNO 1=================")
alumno1.imprimir()
alumno1.resultado()
print("================ALUMNO 2=================")
alumno2.imprimir()
alumno2.resultado()