# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

# Al principio no tiene que haber una opción seleccionada.

from tkinter import *


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))


def reset():
    opcion.set(None)
    monitor.config(text="")


window = Tk()

opcion = IntVar()

Radiobutton(window, text="Opción 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(window, text="Opción 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(window, text="Opción 3", variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(window)
monitor.pack()

Button(window, text="Reiniciar", command=reset).pack()

window.mainloop()







""" Otra Solución
def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Peugeot", variable=opcion, 
            value='Peugeot', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Opel", variable=opcion, 
            value='Opel', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Renault", variable=opcion,   
            value='Renault', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Seat", variable=opcion,   
            value='Seat', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop() """