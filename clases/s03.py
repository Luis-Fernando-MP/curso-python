class Persona:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def hablar(self):
        print(f'Hola soy {self.name}')

class Usuario(Persona):
    vivo = True

    def __init__(self, name, email, password):
        super().__init__(name, email, password)

pepe = Usuario('Pepe', 'pepe@pepe.com', '123456')
pepe.hablar()


"""

Operador	Método especial que lo implementa	Ejemplo
==	__eq__	a == b llama a a.__eq__(b)
!=	__ne__	a != b llama a a.__ne__(b)
<	__lt__	a < b llama a a.__lt__(b)
<=	__le__	a <= b llama a a.__le__(b)


"""