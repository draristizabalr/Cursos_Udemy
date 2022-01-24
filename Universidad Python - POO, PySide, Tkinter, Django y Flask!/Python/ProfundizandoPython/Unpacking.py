# Unpacking o desempaquetado

# Crear un tupla
valores = 1, 2, 3
print(valores, type(valores), sep='\n')

# Crear variables independientes para cada valor
valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

# Se crean varaibles independientes pero se omiten algunos valores
valor1, _, valor3 = 1, 2, 3
print(valor1, valor3)

# Se crean variables independientes pero tambien una lista con el resto de variables faltantes
valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)

# Se crean variables independientes y una lista pero no hasta el final
valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)

# Lo mismo que en el anterior caso pero reemplazando la tupla por una lista
valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

# De igual modo con una función
def regresa_varios_datos():
    return 1, 2, 3

valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *_ = regresa_varios_datos()
print(valor1)

# Partition
print('Metodo \'Partition\''.center(50,'-'))

hora, separador, minutos = '17:20'.partition(':')
print(f'Hora: {hora}, Separador: {separador}, Minutos: {minutos}')
print(type(hora), type(minutos))
