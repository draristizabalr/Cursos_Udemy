# Funciones anidadas
def calculadora(a, b, operacion='suma'):
    # Funcion anidada
    def suma(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # LLamamos a la función anidada
    if operacion == 'suma':
        print(f'Resultado de sumar: {suma(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado de restar: {restar(a, b)}')


calculadora(6, 5)
calculadora(6, 5, operacion='restar')
