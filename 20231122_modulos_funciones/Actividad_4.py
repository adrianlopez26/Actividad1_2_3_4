'''
Crea un módulo con las siguientes clases
Mesa
Silla
Lampara
las tres clases tiene como atributo color y precio.
En otro módulo importa únicamente la clase Silla y crea dos sillas. Una de color azul y otra roja con precios de 9.95

algoritmo funciona:5 puntos
algoritmo utiliza características de POO : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica enumeradores o similar para Color : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

from enum import Enum

class Color(Enum):
    AZUL = 'azul'
    ROJA = 'roja'
    OTRO = 'otro'

class Mueble:
    def __init__(self, color=Color.OTRO, precio=0.0):
        self.color = color
        self.precio = precio

class Mesa(Mueble):
    pass

class Silla(Mueble):
    pass

class Lampara(Mueble):
    pass

'''
Se crea una clase base para que pueda ser heredada por todas las demas mucho mas util.
La programación orientada a objetos (POO):

Organización y encapsulamiento
Reutilización del código
Mantenimiento y escalabilidad
Enumeradores para valores predefinidos
'''