numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares multiplicados por sí mismos
for numero in numeros:
    # Revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)
    else:
        continue

print(f'Lista de numeros pares: {lista_pares}')

# Hacemos lo mismo pero con list_comprehensions
# [expresión for var in colección if condición
# La condición if es opcional
lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Lista de números pares con list_comprehension: {lista_pares}')

# Un ejemplo similar con dos condiciones (las condiciones son opcionales)
# El valor solo se agregará cuando cumpla las dos condiciones
# Es decir, debe ser un numero divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero % 2 == 0 and numero % 6 == 0]
print(f'Lista divisible entre dos(2) y entre seis(6): {pares}')

# Agregar un if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# El mismo ejercicio pero con list_comprehension
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(10)]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# Lista de listas
lista_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# Concertimos la lista de listas en una sola lista
lista_simple = [valor for lista in lista_listas for valor in lista]
print(lista_simple)

# Ahora creamos una lista de números pares a partir de la lista_listas
# Sin list_comprehension, ciclos for anidados
lista_pares = []
for lista in lista_listas:
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            continue
print(f'Lista pares sin list_comprehension: {lista_pares}')
# Con list_comprehension
lista_pares = []
lista_pares = [numero for lista in lista_listas for numero in lista if numero % 2 == 0]
print(f'Lista pares con list_comprehension: {lista_pares}')