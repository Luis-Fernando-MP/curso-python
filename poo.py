class Persona:
  def __init__(self, edad: int, nombre: str) -> None:
    self.edad = edad
    self.nombre = nombre

  def __add__(self, other: 'Persona') -> int:
    if isinstance(other, Persona):
      return self.edad + other.edad
    else:
      raise TypeError("El operando debe ser una instancia de Persona")

# Crear instancias de la clase Personas y ademas de


juana = Persona(edad=20, nombre="Juana")
pepe = Persona(edad=30, nombre="Pepe")

# Sumar las edades de dos personas
suma_edades = juana + pepe
print(f"La suma de las edades es: {suma_edades}")
