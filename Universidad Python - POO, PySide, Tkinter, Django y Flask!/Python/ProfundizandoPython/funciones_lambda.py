# Funciones lambda
# Son funciones anónimas y son pequeñas

def sumar(a, b):
    return a + b

# Con una función lambda (anónima, sin nombre, y una sola linea de código
# No se necesita agregar paréntesis para los parámetros
# No se necesita usar la palabra return, pero si debe regresar una expresión
mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(4, 6)
print(f'El resultado de sumar con funcion lambda: {resultado}')

# Función lambda que no recibe argumentos, pero si regresa una expresión valida
mi_funcion_lambda = lambda: 'Función sin argumentos'
print(f'LLamando la función lambda sin argumentos: {mi_funcion_lambda()}')

# Funciones lambda con parametros default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Resultado argumentos por default: {mi_funcion_lambda()}')
print(f'Resultado argumentos por default: {mi_funcion_lambda(4, 6)}')

# Funciones lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado de argumentos variables: {mi_funcion_lambda(1, 2, 3, a=5, b=6)}')

# Funciones lambda con argumentos, argumentos variables y valores default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado función lambda: {mi_funcion_lambda(1, 2, 4, 5, 6, 7, e=5, f=7)}')7