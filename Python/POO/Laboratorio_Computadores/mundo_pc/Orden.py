from mundo_pc.Computador import Computador

class Orden(Computador):
    contador_orden = 0

    def __init__(self, computadores):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._computadores = computadores

    def agregar_computador(self, computador):
        self._computadores.append(computador)


    @property
    def id_orden(self):
        return self._id_orden

    @property
    def computador(self):
        return self._computadores


    def __str__(self):
        computadores_str = ''
        for computador in self._computadores:
            computadores_str += computador.__str__()
        return f'''
    Orden: {self._id_orden}
    Computadores:{computadores_str}'''



