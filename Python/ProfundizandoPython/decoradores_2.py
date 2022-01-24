def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes de ejecutar la función')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Después de ejecutar la función\n')
        return resultado
    return funcion_decorada_c

@funcion_decorador_a
def sumar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

resultado = sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
print(f'Resultado de la suma: {resultado}')