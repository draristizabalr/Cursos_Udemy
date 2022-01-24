class Empleado:

    def __init__(self, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def sueldo(self):
        return self.sueldo

    @sueldo.setter
    def sueldo(self, sueld):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self._nombre}, Sueldo: ${self._sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()

    def smmlv(self):
        return f'La cantidad de salarios minimos que gana es: ${round(self._sueldo/500, )}'