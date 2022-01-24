# Alcance de variables, también conocido como (scope) en ingles

var_global = 'Variable global'

def imprimir():
    # Acceder una variable global
    global var_global
    print(f'Variable global, pero accedida desde una función: {var_global}')
    # Definición de variable local
    var_local = 'Variable local'
    print(f'Variable local, también accedida desde una función: {var_local}')
    var_global = 'Nuevo valor de la variable global'

    def funcion_anidada():
        print(f'Variable local, dentro de la función anidada: {var_local}')

    funcion_anidada()

imprimir()
print(f'Variable globla fuera de la función: {var_global}')
