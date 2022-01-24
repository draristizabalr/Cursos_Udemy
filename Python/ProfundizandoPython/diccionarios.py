# Profundizando en diccionarios

# Los dict guardan un orden (a diferencia de los set)
diccionario = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 28}
print(diccionario)

# Los dict son mutables, pero sus llaves son inmutables
# diccionario = {[1, 2]: 'Valor'}
# diccionario = {(1, 2): 'Valor'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en una llave de un diccionario (si ya existe se reemplaza)
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)
diccionario['nombre'] = 'David'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# Si no encuentra la llave, lanza una excepción
# print(diccionario['Nombres'])
print(diccionario.get('Nombre', 'No se halló la llave'))
print(diccionario.get('Nombres', 'No se halló la llave'))

# setdefault si modifica el diccionario, si no encuentra la llave en el diccionario
nombre = diccionario.setdefault('Nombres', 'Valor por default')
print(nombre, diccionario, sep='\n')

# Imprimir un diccionario
from pprint import pprint as pp
pp(diccionario, sort_dicts=False)
