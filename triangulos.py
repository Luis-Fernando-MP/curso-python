cantidad: str = ""

while True:
  cantidad = input("Número de filas o 0 para salir\n")
  if not cantidad.isnumeric() or cantidad == "0":
    break
  cantidad = int(cantidad)

  for fila in range(1, cantidad + 1):
    espacios = " " * (cantidad - fila)
    aster = "*" * (2 * fila - 1)
    """
      filas
      * - 2  = 2
      * - 4  = 1
      * - 6  = 0
    """
    print(f'{espacios}{aster}')

