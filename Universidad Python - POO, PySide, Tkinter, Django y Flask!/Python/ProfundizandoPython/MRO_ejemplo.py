class Clase1:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Metodo Clase 1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Método Clase 2')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('Método Clase 3')
        super().metodo()

class Clase4(Clase2, Clase3):
    def metodo(self):
        print('Método Clase 4')
        super().metodo()

# Creamos un objeto de la Clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
# MRO
print(Clase4.__mro__)
# ¿Cuál método se ejecuta?
clase4.metodo()
