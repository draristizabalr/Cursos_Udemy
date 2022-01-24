from FiguraGeometrica import *
from Color import *

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Cuadrado\n{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
