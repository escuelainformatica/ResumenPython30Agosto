import numpy as np

# numpy es un tipo de dato multidimensional, se caracteriza por la velocidad

matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
] # list de lista

datos=np.asarray(matriz) # ndarray

print(datos)
print(datos[1,1]) # una celda (central)
print(datos[:,1]) # columna [2,5,8]
print(datos[1,:]) # fila [4,5,6]
print("---")
print(datos[:2,:]) # [1,2,3] [4,5,6]



