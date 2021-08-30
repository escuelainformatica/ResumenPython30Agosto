import numpy as np
import pandas
import pandas as pd

matriz={
    "col1":[1,2,3],
    "col2":[4,5,6],
    "col3":[7,8,9],
}

valores=pd.DataFrame(matriz,['fila1','fila2','fila3'])

print(valores)
print(valores['col1'].values)
