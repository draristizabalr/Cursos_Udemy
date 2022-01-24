class Rectangulo:
    def __init__(self,altura,ancho):
        self.altura = altura
        self.ancho = ancho

    def mostrar_area(self):
        print(self.altura * self.ancho)

altura = float(input('Proporcionar altura del rectángulo: '))
ancho = float(input('Proporcionar ancho del rectángulo: '))
rectangulo = Rectangulo(altura, ancho)
rectangulo.mostrar_area()
