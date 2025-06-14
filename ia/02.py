"""
  Usando el módulo pandas 
  Se instala con: pip install pandas

  Adicionalmente usaremos seaborn para gráficas
  Se instala con: pip install seaborn


  # Pandas
  Se centra básicamente en manipular objetos de dos tipos:
  - Series: unidimensionales
  - DataFrames: multidimensionales
    Estos dataFrames tienen por columnas a las Series
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""
- Tipo SERIES
"""

# Creando una serie
s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], name='serie1')

# Serie con indices x1, x2...
s2 = pd.Series([1, 2, 3, 4], index=['x1', 'x2', 'x3', 'x4'])

# Serie a partir de un diccionario
s3 = pd.Series({'x1': 1, 'x2': 2, 'x3': 3, 'x4': 4}, )

# Accediendo a los elementos de la serie

s1[1] # Retorna el valor en la posición 1
s2[1:3] # Retorna la serie desde la posición 1 hasta la 3
s1[[1, 3]] # Similar a la anterior
s3['x2'] # Retorna el valor en la posición x2
s3['x2':'x4'] 

# Las Series son de naturaleza matricial, por lo que se pueden operar con matrices

# Para las operaciones entre series los indices deben coincidir
resultadoSerie = s3 + s2 

resultadoSerie2 = np.radians(s1) * np.e

# El parámetro copy es para evitar que se modifique el objeto original
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s4 = pd.Series(arr, copy=True, name='serie4')
s4[0] = 100

"""
- Tipo DataFrame
"""

info = {
  "Pai": ['Argentina', 'Brasil', 'Chile', 'Uruguay'],
  "Pob": [44000000, 210000000, 18000000, 34000000],
  "Sup": [2780000, 8515767, 1760000, 176220]
}

df1 = pd.DataFrame(info)
# Ordenando las columnas
df2 = pd.DataFrame(info, columns=['Sup', 'Pai', 'Pob'])
# Indices personalizados
df3 = pd.DataFrame(info, index=['a', 'b', 'c', 'd'])
# Agregando columnas por vacuidad: Agregara NAN porque no existe
df4 = pd.DataFrame(info, columns=['Pai', 'Pob', 'Sup', 'Deuda'])

# Accediendo a los elementos del DataFrame
df1['Pob'] # Retorna la columna Pob
df1[['Pob', 'Sup']] # Retorna las columnas Pob y Sup


# Accediendo a la filas
df1.iloc[2:3] 
