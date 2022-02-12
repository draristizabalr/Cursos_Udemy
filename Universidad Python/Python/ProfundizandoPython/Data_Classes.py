from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    contador_persona: ClassVar[int] = 0
    domicilio: Domicilio

    # Este código es para verificar que los argumentos dados en el momento de crear un objeto NO sean VACÍOS
    # def __post_init__(self):
    #     if not self.nombre:
    #         raise ValueError(f'Valor nombre vacío: {self.nombre}')
    #     if not self.apellido:
    #         raise ValueError(f'Valor apellido vacío: {self.apellido}')

domicilio1 = Domicilio('Saturno', 15)
persona1 = Persona('Juan', 'Perez', domicilio1)
print(f'Persona 1: {persona1!r}')
# Variable de clase
print(f'Variable de clase: {Persona.contador_persona}')
# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
# Variable con valores vacíos
persona_vacia = Persona('', '', None)
print(f'Persona vacía: {persona_vacia}')
# Revisar igualdad entre objetos
persona2 = Persona('Juan', 'Perez', Domicilio('Jupiter', 30))
print(f'¿Objetos iguales? {persona1 == persona2}')
# Agregar esta clase para una colección
coleccion = {persona1, persona2}
print(coleccion)
# Frozen=True es para no poder mutar ninguno de los elementos del objeto
