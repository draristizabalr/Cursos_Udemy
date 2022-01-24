class DispositivosEntrada:
    def __init__(self, marca, tipoEntrada):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @property
    def marca(self):
        return self._marca

    def __str__(self):
        return f'marca: {self._marca}, tipo_entrada: {self._tipoEntrada}'

    def mostrar_detalles(self):
        return self.__str__()

