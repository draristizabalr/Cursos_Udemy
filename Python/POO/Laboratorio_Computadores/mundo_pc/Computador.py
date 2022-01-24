class Computador:
    contador_computador = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computador.contador_computador += 1
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        self._id_computador = Computador.contador_computador

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    @property
    def id_computador(self):
        return self._id_computador

    def __str__(self):
        return f'''
    {self._nombre}: {self._id_computador}
    Monitor: {self._monitor}
    Teclado: {self._teclado}
    Ratón: {self._raton}\n'''