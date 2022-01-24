class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre # Si el atributo tiene un guión bajo no se debe acceder a el
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

    # Función GET para el atributo (nombre)
    @property
    def nombre(self):
        return self._nombre

    # Función SET para el atributo (nombre)
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    # Destructor de objeto personalisado
    def __del__(self):
        print(f'Persona: {self._nombre} {self.apellido}')


if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28, '3215416516', 2, 3, 4, 5, m='Manzana', p='Pera', n='Naranja')
    persona1.mostrar_detalle()

    persona2 = Persona('Carla', 'Gomez', 30)
    persona2.mostrar_detalle()
