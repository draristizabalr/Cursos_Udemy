from mundo_pc.DispositivosEntrada import DispositivosEntrada

class Raton(DispositivosEntrada):
    contador_mouse = 0

    def __init__(self, marca, tipoEntrada):
        Raton.contador_mouse += 1
        DispositivosEntrada.__init__(self, marca, tipoEntrada)
        self._id_mouse = Raton.contador_mouse

    @property
    def id_mouse(self):
        return self._id_mouse

    def __str__(self):
        return f'ID: {self._id_mouse} {DispositivosEntrada.__str__(self)}'
