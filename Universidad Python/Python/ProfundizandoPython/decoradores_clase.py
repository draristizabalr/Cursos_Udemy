# Decoradores de clase
# Permiten transformar de forma programatica nuestra clase
# Es similar a los decoradores de funciones (es metaprogramación)
import inspect


def decorador_repr(cls):
    print('Se ejecuta el decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de nuestra clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo
    for nombre, atributo in atributos.items():
        print(nombre, atributo)

    # Revisamos si se ha sobreescrito __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma del método __init__: {firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros init: {parametros_init}')

    # Revisar si por cada parámetro tiene su método property asociado
    for parametro in parametros_init:
        es_property = isinstance(atributos.get(parametro), property)
        if not es_property:
            raise TypeError(f'No existe un método property para el parámetro indicado: {parametro}')

    # Crear método repr dinámicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        # Expresión generadora, crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # Lista de argumentos
        lista_argumentos = list(generador_arg)
        print(f'Lista del generador: {lista_argumentos}')
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_argumentos)
        print(f'Argumentos del método repr: {argumentos}')
        # Creamos la forma del método __repr__, sin su nombre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado de ejecutar método repr: {resultado_metodo_repr}')
        return resultado_metodo_repr

    # Agregar dinámicamente el método repr
    setattr(cls, '__repr__', metodo_repr)

    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

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

    @property
    def edad(self):
        return self._edad

    # def __repr__(self):
    #     return f'Persona(Nombre={self._nombre}, Apellido={self._apellido})'

persona1 = Persona('David', 'Aristizábal', 29)
print(persona1)

persona2 = Persona('Paola', 'Correa', 32)
print(persona2)

# Tiene los métodos de propiedad: nombre, apellido, edad, repr
print(dir(Persona))

# Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)