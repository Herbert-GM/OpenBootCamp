#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

# python code to demonstrate working of reduce()
 
# importing functools for reduce()
import functools
 
 # The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
 # The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.

def ej2(lista): 
    resultado = list(filter((lambda x: x % 2), lista)) 
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)

# initializing list
lista = list(range(100))

ej2(lista)