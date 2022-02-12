# Un closure es una función que define a otra, y además regresar la función anidada puede acceder
# a las variables locales definidas en la función principal o externa

# Función operación
def operacion(a, b):
    # Definimos una función interna o anidada
    def sumar():
        return a + b

    # Returnar la función
    return sumar

mi_función_closure = operacion(5, 2)
print(f'Resultado de la función closure: {mi_función_closure()}')

# Llamar la función regresada al vuelo
print(f'resultado de la función closure ejecutada al vuelo: {operacion(2, 3)()}')

# Función lambda
def operacion(a, b):
    # 1. Definimos una función lambda o anidada y la retornamos
    return lambda: a + b

mi_función_closure = operacion(5, 2)
print(f'Resultado de la función closure: {mi_función_closure()}')

# Llamar la función regresada al vuelo
print(f'resultado de la función closure ejecutada al vuelo: {operacion(4, 5)()}')

