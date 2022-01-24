# Orden de inicialización de objetos
class Padre:
    def __init__(self):
        print('Inicialización Padre')

    def metodo(self):
        print('Método padre')

class Hijo(Padre):
    # Se manda a llamar el método init, siempre y cuando la clase padre no mande a llamar el método init
    def __init__(self):
        # De manera opcional se puede llamar el método init del padre (super)
        print('Inicializando hijo')
        super().__init__()

    # Sobreescribimos el método heredado de la clase padre
    def metodo(self):
        print('Método sobreescrito hija')
        super().metodo()

hijo1 = Hijo()
hijo1.metodo()