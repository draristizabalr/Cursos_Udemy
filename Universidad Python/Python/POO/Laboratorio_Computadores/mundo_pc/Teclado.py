from mundo_pc.DispositivosEntrada import DispositivosEntrada

class Teclado(DispositivosEntrada):
    contador_teclado = 0

    def __init__(self, marca, tipoEntrada):
        DispositivosEntrada.__init__(self, marca, tipoEntrada)
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado

    @property
    def id_teclado(self):
        return self._id_teclado

    def __str__(self):
        return f'ID: {self._id_teclado} {DispositivosEntrada.__str__(self)}'