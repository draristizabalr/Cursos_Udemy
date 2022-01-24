# Generador de numeros del 1 al 5
def generador_de_numeros():
    for numero in range(1, 6):
        yield numero
        print('Se reanuda la ejecución de la función.')

# Utilizamos el generador
generador = generador_de_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

# Consumimos los valores del generador
for valor in generador:
    print(f'Numero producido: {valor}')

# Otra forma de consumir un generador
generador = generador_de_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresion del valor generado: {valor}')
    except Exception as e:
        print('Se terminó de iterar el generador')
        break