# Representacion de objetos (str, repr, format)

class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # repr, más enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre={self._nombre}, apellido={self._apellido})'

    # str, más para el usurio final o para otros sistemas
    def __str__(self):
        return f'{self.__class__.__name__} [Nombre: {self._nombre} - Apellido: {self._apellido}]'

    # format
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self._nombre} y apellido {self._apellido}'

persona1 = Persona('Juan', 'Perez')
# repr
print(f'Mi objeto Persona: {persona1!r}')
# str (de manera automática el método print llama al método str)
print(persona1)
# format (con un f string se llama de forma automática)
print(f'{persona1}')