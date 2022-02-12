class Monitor:
    contador_monitor = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._marca = marca
        self._tamaño = tamaño
        self._id_monitor = Monitor.contador_monitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    @property
    def id_monitor(self):
        return self._id_monitor

    def __str__(self):
        return f'ID: {self._id_monitor} marca: {self._marca}, tamaño: {self._tamaño} pulgadas'

    def mostrar_detalles(self):
        return self.__str__()
