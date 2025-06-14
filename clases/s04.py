"""
  # Patrones de diseño:
  Consisten en soluciones a problemas comunes que se repiten en el desarrollo de software, y que se pueden aplicar en cualquier proyecto.

  * Patrones creacionales (Básicamente tratan con la creacion de objetos, y tienen que ver con la creacion de objetos):
   - Patron abstract factory
   - Patron prototype
   - Patron singleton 

  * Patrones estructurales (Básicamente tratan con la composicion de objetos, y tienen que ver con la composicion de objetos):
   - Patron adapter
   - Patron bridge
   - Patron composite
   - Patron decorator
   - Patron facade
   - Patron proxy

  * Patrones comportamentales (Basicamente tratan con algoritmos y la asignacion de resposabilidades entre objetos, ):
   - Patron observer
   - Patron strategy
   - Patron state
   - Patron visitor
   - Patron iterator
   - Patron visitor

  * Patrones de diseño en python
   - Patron facade
   - Patron singleton 

  ---

# Aquitectura  de software:
  Consiste en la estructura de un software, y en la organizacion de sus componentes, y en la manera en que se comunican entre ellos. Algunos tipos comunes de estos son:

  * Monolítica: Es un software que tiene una sola unidad de responsabilidad. Es decir, que todos los componentes del software tienen una sola responsabilidad.

  * De microservicios: La aplicacion se divide en peques servicios independientes que pueden desarrollarse y desplegarse de manera independiente

  * De capas: Separando la logica de presentacion de la logica de negocio 

  * Clean Arquitecture: Se enfoca en la separacion de responsabilidaddes, la independencia de frameworks y la facilidad de prueba, manteniendo la logica de negocio en el nucleo

  ---
  # Pincipio solid, se basa en los 5 principio: SRP (cada clase tiene un unica responsabilidad), OCP (Las clases deben de estar abiertas para la extension, pero cerradas para modificcacion), de sustitucion, donde los objetos de una clase derivada deben de poder sustituir los elementos de la clase padre sin alterar la funcoonalidad del programa, Principio de segregacion de interfaces, una clase no deberia de estar forzada a implementar interfaces que no usa. Principio de inversion, las clases deben de depender de abstracciones y no de concreciones  

"""


"""
  Monkey patcching adicion dinaimca en tiempo de ejecucion 
"""