"""
  Clase 02: Manejo de Archivos en memoria RAM
"""

file_path = "tmp/names.csv"

"""
# Descargar el archivo CSV desde la URL usando wget

from os import system   
csv_name = "https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/refs/heads/master/shot.csv"

system(f'wget -O {file_path} {csv_name}')
"""

import csv  

"""
  Usamos el contexto 'with' de python para abrir el archivo,
  a diferencia de otras librerías como pandas o pyspark,
  el archivo no se carga en memoria, sino que se va leyendo
  linea por linea, lo que permite trabajar con archivos grandes
  sin necesidad de cargar todo el archivo en memoria. Ademas en esas librerías
  se considera que el número de filas es el número de registros es el mismo
"""
with open(file_path, 'r') as file:
  reader = csv.reader(file)
  people = {} 
  for row in reader:
    if row[1] == 'Name': continue

    people[row[1]] = people.get(row[1], 0) + 1

def count_names(names_list: dict, character: str):
  count = 0
  for name in names_list:
    if name.lower().startswith(character.lower()):
      count += 1
  return count



print(count_names(people, 'a'))


"""
  Parámetros con * y kwargs
"""
def print_names_with_prefix(prefix, *names, **kwargs):
  """
  Imprime los nombres que comienzan con un prefijo dado.
  También puede aceptar argumentos adicionales a través de kwargs.
  """
  case_sensitive = kwargs.get('case_sensitive', False)
  for name in names:
    if case_sensitive:
      if name.startswith(prefix):
        print(name)
    else:
      if name.lower().startswith(prefix.lower()):
        print(name)

# Ejemplo de uso
print_names_with_prefix('A', 'Alice', 'Bob', 'Anna', 'Andrew', case_sensitive=False)


"""
  Lanzando excepciones con raise
"""

def get_number():
  raise Exception('Error message')