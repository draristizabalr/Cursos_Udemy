# Las funciones en python son ciudadanas de primera clase
# First class citizens

# Definimos la función
def sumar(a, b):
    return a + b

# 1. Asignar una función a una variable
mi_funcion = sumar

# Verificar el tipo de la variable
print(type(mi_funcion))

# Llamamos la función a traves de la variable
resultado = mi_funcion(5,8)
print(f'Resultado: {resultado}')

# Función como argumento
def operacion(a, b, sumar):
    print(f'Resultado de sumar: {sumar(a, b)}')

operacion(4, 5, sumar)

# 3. Podemos retornar una funcion
def retornar_funcion():
    # Retornamos una funcion
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado de la función retornada: {mi_funcion_retornada(5, 7)}')