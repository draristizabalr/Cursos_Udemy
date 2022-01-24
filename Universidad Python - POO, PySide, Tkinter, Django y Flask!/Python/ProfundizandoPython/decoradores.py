# Decoradores
# Un decorador es una función que recibe una función y regresa otra
# Lo utilizamos para extender funcionalidad
# 1. Función decorador (a)
# 2. Función decoradora (b)
# 3. Función decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c():
        print('Antes de ejecutar la función')
        funcion_a_decorar_b()
        print('Después de ejecutar la función\n')
    return funcion_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde función mostrar_mensaje')

@funcion_decorador_a
def imprimir():
    print('Hola desde función imprimir')

mostrar_mensaje()
imprimir()