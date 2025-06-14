frase = "Hola mundo como estamos"

def contar_letras(text: str = frase):
  new_list = list(text.replace(' ', ''))
  dictionary = {}

  for i, letter in enumerate(new_list):
    # print(f"letra {letter} indice {i}")
    dictionary[letter] = dictionary.get(letter, 0) + 1

  sorted_dict = dict(sorted(dictionary.items(), key= lambda item: item[1], reverse=True))

  return sorted_dict

contar_letras()


mi_diccionario = {x: x**2 for x in range(5)}


miDic = {i: var for i, var in enumerate(range(10), start=100)}

print(miDic)  
