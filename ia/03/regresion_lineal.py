path = 'ia/03/bikes.csv'
""" Descargando el archivo csv
csv_url = "https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/refs/heads/master/bikes.csv"
from os import system

system(f'wget -O {path} {csv_url}')
"""

"""
MODELO DE REGRESIÓN LINEAL MÚLTIPLE
1. Particionamiento de datos: Si uno quiere a partir de los datos, construir una formula matemática que para datos nuevos de las variables independientes, poder pronosticar la variable dependiente, con lo cual se opta por Seder el mayor subconjunto de los datos al paso 1, aplicando la regla de Pareto (que no es absoluta si no mas bien, es ajustable a nuestros requerimientos), el 80% serian de entrenamiento

2. Subconjunto de testeo: 20% de los datos para el testo 
"""

import pandas as pd

# train_test_split para el primer paso: Particionar el data center
from sklearn.model_selection import train_test_split

# Para el primer caso: para un aprendizaje supervisado y cuantitativo
# Regresión lineal
from sklearn.linear_model import LinearRegression

#Finalmente para calcular los indicadores de calidad usamos
from sklearn import metrics

bikes = pd.read_csv(path)

# Nuestra variable dependiente para el caso sera Rentals (alquiler)
y_data = bikes.rentals

# Variables independientes, Axis 1 porque borramos la columna que esta en 2 dimensiones
x_data = bikes.drop('rentals', axis=1)






"""
  La función train_test_split retorna 4 parámetros

  1. x_train: subconjunto de variables independientes para entrenar el modelo
  2. x_test: subconjunto de variables independientes para testear el modelo

  3. y_train: subconjunto de observaciones de la variable dependientes para entrenar el modelo
  4. y_test: subconjunto de observaciones de la variable dependientes para testear el modelo
"""

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.8)


model = LinearRegression()

model_base = model.fit(x_train, y_train)


"""
  2. indicador de calidad, se separa en dos etapas:
    - que tanto ha aprendido el modelo
    - 

"""

y_test_forecast = model_base.predict(x_test)

mape_base = metrics.mean_absolute_percentage_error(y_test, y_test_forecast)

print(f'El porcentaje de errores es {mape_base * 100}')