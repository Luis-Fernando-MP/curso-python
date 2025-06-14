Modelo de aprendizaje automático: Este se centra en dos tipos de problemas:

# 1. Teniendo una variable dependiente:

### Problema de aprendizaje supervisado:

- Significa que buscamos aproximarnos mediante un modelo de un conjunto de variables independientes, es decir:

```python
y = aprox_modelo(x1, x2, x3 ... xn)
```

- En este punto tendríamos dos casos:
  - Y es cuantitativa: Entonces estamos frente a un problema de regresión lineal (vale verificar que aun siendo un número nuestra variable no se podría considerar al 100 como cuantitativa, pues se debería de abordar por su diversificación, ya que no es lo mismo por ejemplos números del 1 al 7 'semana' que una serie de números diferentes)
  - Y es cualitativa: Problema de clasificación

## Según la literatura

- Modelo de regresión lineal simple: si tienes 1 variable independiente y 1 variable dependiente
- Modelo de regresión lineal multiple: más de 1 variable independiente

2.  No teniendo una variable dependiente

# -> Problema de aprendizaje no supervisado:

    * Entonces nos centramos en la forma de encontrar un patron, encontrar una forma de clasificar al conjunto de variables que tengamos
    * Clasificar/particionar al conjunto de datos en sub-conjuntos cuyos elementos tengan propiedades similares

Para todo ello Scikit-Learn nos sera de mucha ayuda, contamos con 3 tareas: 1. Particionar nuestro data center: - Subconjunto de datos para entrenar un modelo: Para la obtención de los parámetros del modelo - Subconjunto de datos para testear: Para un indicador de calidad

    2. Instancia y ajuste de una clase a ajustar
    3. Calcular los indices de calidad: Si es que el modelo actual cumple o no, con nuestras expectativas

pip install scikit-learn

# Para el primer ejemplo de Aprendizaje supervisado, cuantitativo:

- Revisa el documento de ./regresión_lineal.py
