def fibonacci (limit = 10, list = [0, 1]):
  if(len(list) >= limit): return list
  new_num = list[len(list) - 2] + list[len(list) - 1]
  list.append(new_num)

  return fibonacci(limit, list)

# print(fibonacci())
def MCD(a: int, b: int) -> int:
  """
  Calcula el Máximo Común Divisor usando el algoritmo de sustracción.
  """
  while b != 0:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a

print(f"MCD(9, 3) = {MCD(9, 3)}") 
print(f"MCD(48, 18) = {MCD(48, 18)}")   
print(f"MCD(7, 13) = {MCD(7, 13)}") 
print(f"MCD(0, 5) = {MCD(0, 5)}") 