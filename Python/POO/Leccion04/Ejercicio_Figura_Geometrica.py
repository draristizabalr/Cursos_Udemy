from Cuadrado import *
from Rectangulo import *

figura1 = FiguraGeometrica(5, 4)
color1 = Color('Verde')
cuadrado1 = Cuadrado(5, 'Violeta')
rectangulo1 = Rectangulo(2,6,'Morado')

print(figura1, color1, cuadrado1, cuadrado1.area(), rectangulo1, rectangulo1.area(), sep='\n')