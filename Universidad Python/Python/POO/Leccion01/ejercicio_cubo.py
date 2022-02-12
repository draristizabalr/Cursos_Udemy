class Cubo:
    def __init__(self,alto,ancho,largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def volumen(self):
        print(f'El volumen es: {self.alto * self.ancho * self.largo}')

alto = float(input('Proporcionar el alto del cubo: '))
ancho = float(input('Proporcionar el ancho del cubo: '))
largo = float(input('Proporcionar el largo del cubo: '))

cubo = Cubo(alto,ancho,largo)
cubo.volumen()
