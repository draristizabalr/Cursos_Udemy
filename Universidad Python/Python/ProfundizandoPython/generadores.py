# Generadores
# Es una función especial, retorna una secuencia de valores
# suspende la ejecución de la función yield (producir) (no se usa return)

def generador():
    yield 1
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda la ejecución')
    yield 3

# Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# Si intentamos consumir más valores de los que produce nuestro generador produce un error
# print(next(gen))

# Consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Numero generado: {valor}')
