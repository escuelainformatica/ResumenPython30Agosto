from decimal import Decimal
import Ejemplo1

# import Ejemplo2 # importo ambas funciones
                # Ejemplo2.funcion1()
from Cliente import Cliente
from Ejemplo2 import funcion1
                # funcion1()
from Ejemplo2 import  funcion2 as f2
                # f2()

# variables
from Libro import Libro

entero = 20
texto = "hola"
texto2 = 'hola'
flotante= 20.4 # flotante (inexacto) 20.3999999999
decimal=Decimal(20.4) # decimal exacto
booleano= True

textoNulo = None # nulo
textoVacio = ""  # vacio
# texto = # Numpy.NaN nulo de numpy

# type hinting

texto3:str="hola"

# funciones

def mifuncion(argumento):
    return "hola mundo"

mifuncion(20)

def mifuncionv2(argumento:int)->str:
    return "hola mundo"

# variables tienen mas de un valores.

tuples=(1,2,3,4)  # es rapido pero solo de lectura.
listado=[1,2,3,4] # es lento pero es editable
registros={1,2,3,4,4}  # no guarda duplicados, y no tiene un concepto de orden
diccionarios={'hola':1,'mundo':2} # es mas facil leer una columna determinada, que un numero de columna

print(tuples[0]) # el primer valor de tuple.
print(listado[0]) # el primer valor del listado
print(registros) # mostrar to do el registro
print(diccionarios['hola'])

# args, kwargs
def mostrarargumentos(*tuple): # empaquetar
    print("esta es la funcion:")
    for fila in tuple:
        print(fila)


mostrarargumentos(1,2,3)

mituple=(1,2,3)
mostrarargumentos(mituple[0],mituple[1],mituple[2])

def segundafuncion(**kwargs): # se empaqueta los argumentos con nombre en un diccionario
    print("esta es la segunda funcion:")
    print(kwargs)
    for llave in kwargs:
        print(llave,kwargs[llave])

mostrarargumentos(*mituple) # lo desempaqueto.

segundafuncion(argumento1="hola",argumento2="mundo")

# usando las clases

john=Cliente() # una variable definida por una clase se llama objeto
john.rut="1-9"
john.nombre="john"
john.edad=33
print(john.nombre)

johnkg=Cliente(rut="1-9",nombre="john",edad=33)

johndic={"rut":"1-9","nombre":"john","edad":33}
print(johndic['nombre'])

johntuple=("1-9","john",33)
print(johntuple[1])

# ejercicio libro y herencia

harry=Libro()
harry.titulo="Harry potter"
harry.cant_paginas=200
harry.autor="autor1"
harry.mostrar()

# funciones
def funcion_nueva():
    return "funcion nueva"
print("---ejercicio funcion---")
print( funcion_nueva() ) # llamando a la funcion
print( funcion_nueva ) # indicando la funcion

# pasos de la progracion funcional
variable2=funcion_nueva # la variable2 es la funcion
print(variable2()) # llamando a la funcion















