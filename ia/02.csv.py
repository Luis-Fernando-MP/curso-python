path = 'tmp/heart.csv'

""" Descarga el archivo de csv
from os import system    

csv_url = "https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/refs/heads/master/HeartDisease2022.csv"
system(f'wget -O {path} {csv_url}')
--------------------------------
"""

"""
  Manejando archivos con pandas
"""

import pandas as pd

# usando el método readCsv, sus ventajas son 
csv = pd.read_csv(path)
# type(csv) <-- lo lee como un DataFrame

# Sin leer las cabeceras, pero si las carga 
# csv_2 = pd.read_csv(path, header=None, low_memory=False)

# Accediendo a las columnas, esta es un columna
csv.columns 
for col in csv.columns:
    col

# Pintando los las cabeceras que ten h, de la forma mas corta posible
# csv.columns[]
columnas_con_h = csv.columns.str.startswith('H')
csv.columns[columnas_con_h]


# Buscando los datos faltante
csv.isnull().sum() # Regresa una Serie
csv.isnull().sum().sum() # Regresa una Serie


# Eliminando los datos faltantes
csv.dropna(inplace=True)


# Eliminando los datos duplicados
csv.drop_duplicates(inplace=True)

# Leyendo los tipos de datos
csv.dtypes

# Buscando los datos faltantes
csv_f = csv.select_dtypes(include=['float64'])


# Cortando filas
csv.head(10) # Los primeros 10
csv.tail(10) # Los últimos 10
csv.sample(10) # 10 filas aleatorias
csv.sample(frac=0.5) # 50% de las filas
csv.sample(frac=0.5, random_state=123) # 50% de las filas, pero con un random_state
csv.sample(axis=1) # 1 columna aleatoria
csv.sample(n=10, axis=1) # 10 columnas aleatorias




# Percentiles: un percentile significa que se divide el conjunto de datos en 100 partes iguales
# percentiles = csv.quantile(q = [0.25, 0.5, 0.75])

# print(percentiles)



# Hallando la desviación estándar
cumplen = csv.loc[csv['haui'] < 100000]
des = cumplen.select_dtypes(include=['float64']).std()




# media aritmética
media = csv['haui'].mean()


# Unique nos muestra los valores únicos de una columna con True, False
unique = csv['haui'].unique()



# Group by
tmpGroup = csv.groupby('GeneralHealth')[csv_f.columns].mean()
print(tmpGroup)


"""
  Graficando con matplotlib
"""

import matplotlib.pyplot as plt

# mostrar cuantos hombre y mujeres hay en el dataset
csv['Sex'].value_counts().plot(kind='bar')
plt.savefig("imgs/haui_line.png") 