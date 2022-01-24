# Más funciones anidadas y alcance de variables

def funcion_externa():
    variable_local_externa = 'Variable local externa'
    print(f'Valor variable local externa: {variable_local_externa}')

    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'

        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor variable local externa'

    funcion_anidada()
    print(f'Valor variable local externa: {variable_local_externa}')
    # print(f'Valor variable local anidada: {variable_local_anidada}')
    # No se puede acceder a esta variable, ya que se destruye al salir del bloque de función anidada
funcion_externa()