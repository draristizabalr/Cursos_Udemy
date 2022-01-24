numeros = [1, 2, 3]
letras = ['a', 'b', 'c', 'd', 'e']
indicadores = 321, 322, 323, 324, 325
conjunto = {6, 4, 0, 9, 8, 15, 10}
mezclas = zip(numeros, letras, indicadores, conjunto)

print(mezclas)
print(list(mezclas))
print(tuple(mezclas))
print(tuple(zip(numeros,letras)))
print(type(mezclas))


# Iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, indicadores, conjunto):
    print(f'Numero: {numero}, Letra: {letra}, ID: {id}, Aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, indicadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)

# Unzip
mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*mezcla)
print(f'Numeros: {numeros} Letras: {letras}')

# Ordenamiento usando zip
letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3, 2, 4, 1, 0]
mezcla = zip(letras, numeros)
print(tuple(mezcla))
# Ordenar por letra
print(sorted(zip(letras, numeros)))

# Crear un diccionario con zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

# Actualizar un elemento de una diccionario
llave = ['Edad']
valor = [28]

diccionario.update(zip(llave, valor))
print(diccionario)