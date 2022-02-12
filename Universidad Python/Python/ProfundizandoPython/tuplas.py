# Profundizando en tuplas

# Declarar variables
a, b = 'Hola', 'Adios'
print(a, b)
# swap
a, b = b, a
print(a, b)

# Regresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax([1, 2, 3, 4, 5])
print(f'Valor mínimo: {min} Valor máximo: {max}')

# Regresar la suma de una tupla
resultado = sum((1, 2, 3, 4, 5))
print(resultado)

def sumar(*args):
    return sum(args)

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)
