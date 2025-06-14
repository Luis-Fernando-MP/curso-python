# Abraham Zamudio
"""
Si para las personas el termino aprender resulta confuso, este mismo termino para un sistema computacional es algo ambiguo, sin embargo, son estos mismos sistemas mas potententes y eficientes los que nos permiten resolver de forma eficiente problemas que antes solo nos parecían imposibles

Este conocimiento consiste en pasar de un análisis retrospectivo a un análisis predictivo, es decir, predecir el comportamiento futuro de un sistema o un proceso.
E incluso a un análisis prescriptive, es decir, establecer una estrategia de acción para el futuro.


numpy numeric python
para formular un problema este debe de estar formado en forma de matriz

random     --> Herramientas aleatorias básicas
linalg     --> Herramientas básicas de álgebra lineal
fft        --> Para las transformadas de Fourier 
polynomial --> Herramientas polinómicas
"""

import numpy as np

# Ejemplo hallando la determinante de una matriz
# matriz = np.random.randint(10, 20, size=(3,3))
# print(f"""Resultado: 
# {matriz}
# Determinante: {np.linalg.det(matriz)}
# """)

# Manejando arreglos
arr = np.array([20, 60, 90, 180])

arr2 = np.array([[10, 12],
                [15, 18]])

# Shape: sirve para conocer el número de filas y columnas
# print(arr.shape) Salida: (4,)
# print(arr2.shape) Salida: (2, 2)

# Los arreglos en numpy son vectorizadas, por lo que hacer algo como suma, sumaria a cada item del vector
# print(arr + 10) Salida : [30, 70, 100, 190]
# print(arr2 + 10) Salida: [[20. 22.] [25. 28.]]

# Hallando el seno para cada elemento del arreglo, ojo el sin acepta valores en radianes
# print(np.sin(np.radians(arr))) # Salida: [0.84147098 0.90929743 0.14112001]

# --------------------------------
# La Regla de correspondencia significa que si hay una relación entre dos variables, es posible hacer una regresión lineal de estas variables

# linspace sirve para crear un arreglo con números equiespaciados y equiespaciados significa que los valores van de un inicio a un final con un número de elementos que se le indique

datosA = np.linspace(10, 20, 10)
datosB = np.exp((4 * datosA) / (datosA **(4.9)))
longitud = len(datosB)

# para visualizar los datos usamos la librería matplotlib.pyplot, esta se instala con pip install matplotlib
import matplotlib.pyplot as plt

""" Gráficos con la función plot
plt.figure()# Inicia una nueva imagen
plt.plot(datosA, datosB)
plt.savefig("imgs/graph.png") 

plt.clf() # limpia la imagen anterior

# Agreguemos a la señal/datos almacenados en el objeto datosB un peque ruido 

plt.figure() 
plt.plot(datosA, datosB + (np.random.random(longitud) * 10**(-4)))
plt.savefig("imgs/ruido.png") 
"""
""" Gráficos simultáneos (sin limpiar el plt)

plt.style.use("dark_background") 
plt.figure()
plt.plot(datosA, datosB, label="Datos", color="red", linestyle="dashed", linewidth=2, marker="o", markersize=10, markerfacecolor="blue", markeredgecolor="red")

plt.plot(datosA, datosB + (np.random.random(longitud) * 10**(-4)), label="Ruido")
plt.title("Gráfica de datos")
plt.xlabel("Datos A")
plt.ylabel("Datos B")
plt.legend()
plt.savefig("imgs/unidos.png") 

# Style te muestra la lista de estilos de matplotlib
print(plt.style.available)
"""

# Gráfico de barras
x1 = np.array([10, 20, 30, 40, 50])
y = x1 ** 2

plt.figure(figsize=(16, 9))
plt.title("Gráfica de barras", fontdict={"fontsize":15, "color": "red", "weight": "bold", "style": "italic", "variant": "small-caps"})
plt.bar(x1, y)
plt.savefig("imgs/bar.png")