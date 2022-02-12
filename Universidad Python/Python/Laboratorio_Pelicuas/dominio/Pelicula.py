class Pelicula:
    numero_pelicula = 0

    def __init__(self, nombre):
        Pelicula.numero_pelicula += 1
        self._nombre = nombre

    @property
    def nombre(self):
        return nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula {Pelicula.numero_pelicula}: {self._nombre}'
