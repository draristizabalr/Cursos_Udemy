from Cuadrado import *

cuadrado1 = Cuadrado(5, 'Rojo')
print(cuadrado1.alto)
print(cuadrado1.ancho)
print(cuadrado1.color)
print(cuadrado1.area())

# MRO - Method Resolution Object
print(Cuadrado.mro())