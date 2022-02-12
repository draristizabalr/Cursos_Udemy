# Expresión generadora (es un generador anónimo)

multiplicacion = (valor*valor for valor in range(4))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

# También se puede pasar una expresión generadora a una función (sin parentesis)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado de la suma: {suma}')

# También podemos usar una lista o cualquier otro iterador
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un str a partir de una generador
lista = ['Karla', 'Gomez']
contador = 0
# Definimos una función para aumentar el contador
def aumentar_contador():
    global contador
    contador += 1
    return contador
# La primera para el yield, la segunda es el for, entre parentesis
generador = (f'{aumentar_contador()}.{nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada a partir de la lista: {cadena}')
