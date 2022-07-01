# PYTHON

## Control de flujo:

* `True or False`

~~~python
a = 5
b = 6
C = 7

resultado = a == b

resultado = (a > 5 and c < 7)
# resultado = (False and c < 7)
# resultado = (False and False)
# resultado = (False)
print(resultado)
~~~

* **Tabla de la verdad**

~~~python
# AND -> True, False
print("t y t", True and True)
print("t y f", True and False)
print("f y t", False and True)
print("f y f", False and False)

print()

# OR -> True, False
print("t o t", True or True)
print("t o f", True or False)
print("f o t", False or True)
print("f o f", False or False)

print()

# XOR -> True, False
print("t xor t", True ^ True)
print("t xor f", True ^ False)
print("f xor t", False ^ True)
print("f xor f", False ^ False)
~~~

## Condicionales:
~~~python
if condicion:
    acciones en if 1
    acciones en if 2
elif otra condicion
    acciones en otra condicion
acciones fuera del if
~~~