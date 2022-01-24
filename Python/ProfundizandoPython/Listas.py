# Profundizando en listas
# Las listas son mutables

nombres1 = ['David', 'Pedro', 'Carmenza', 'Jaime']
nombres2 = 'Paola Elisa Hector Patricia'.split()
print(f'Nombres 1: {nombres1}', f'Nombres 2: {nombres2}', sep='\n')

# Sumar listas
print(f'Sumar listas: {nombres1 + nombres2}')

# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista 1 con la lista 2: {nombres1}')

# Lista de números
numeros1 = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista oroginal: {numeros1}')

# obtener el indice del primer elemento encontrado en una lista
print(f'Indice 4: {numeros1.index(4)}')

# Invertir el orden de la lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenar los elementos de una lista de manera ascendente
numeros1.sort()
print(f'Lista ordenada (ascendente): {numeros1}')
# Ordenar los elementos de una lista de manera descendente
numeros1.sort(reverse=True)
print(f'Lista ordenada (descendente): {numeros1}')

# Obtener valor mínimo de una lista
print(f'Valor mínimo: {min(numeros1)}')
# Obtener valor máximo de una lista
print(f'Valor máximo: {max(numeros1)}')

# Copiar los elementos de una lista
numeros2 = numeros1.copy()
print(numeros1, numeros2, sep='\n')
print(f'¿Misma referencia? {numeros1 is numeros2}')
print(f'¿Mismo contenido? {numeros1 == numeros2}')

# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f'¿Misma referencia? {numeros1 is numeros2}')
print(f'¿Mismo contenido? {numeros1 == numeros2}')

# slicing
numeros2 = numeros1[:]
print(f'¿Misma referencia? {numeros1 is numeros2}')
print(f'¿Mismo contenido? {numeros1 == numeros2}')

# Multiplicación de listas
lista_multiplicacion = 5*[[2, 5]]
print(lista_multiplicacion)
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)
# Al modificar una de las listas creadas en la linea 55 modificamos todas a las vez
# Dado que los objetos de lista al crearse tomaron caracteristicas compartidas

# Matrices
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglon 0, Columna 0: {matriz[0][0]}')
print(f'Renglon 2, Columna 2: {matriz[2][2]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
lista_listas.sort(key=len)
print(f'Ordenar por cantidad de elementos: {lista_listas}')

# sorted built-in
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)
nombres1 = sorted(nombres1, key=len)
print(nombres1)
