# bool contiene valores de True y False
# Tipos numéricos, False para 0, True demás valores
# Funciona para cualquier tipo de numero: int o float

valor = 0
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 15
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

# Tipo str, False para '' y True para cualquier valor
valor = ''
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 'Hello world'
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

# Para colecciones el resultado será False para colecciones vacías y será True para el resto de colecciones
# Listas
valor = []
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = [1, 2, 3]
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = (1, 2, 3)
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = {'Horas': 8, 'Minutos': 23, 'Segundos': 34}
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

if 'Hola':
    print('Regresa verdadero')
else:
    print('Regresa falso')

if bool('Hola'):
    print('Regresa verdadero')
else:
    print('Regresa falso')

valor: 0

while valor:
    print('Ejecución del ciclo while')
else:
    print('Fin ciclo while')