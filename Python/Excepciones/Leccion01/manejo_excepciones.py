from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('numeros idénticos')
    resultado = a / b
except  ZeroDivisionError as e:
    print(f'Ocurrio un error:\n{e}')
except TypeError as e:
    print(f'Ocurrio un error:\n{e}')
except Exception as e:
    print(f'Ocurrio un error:\n{e}')
# Se ejecuta cuando NO hay errores
else:
    print('Datos ingresados correctamente')
# El bloque finally SIEMPRE se va a ejecutar, sea si hay un error o no
finally:
    print('Ejecutando bloque "finally"')

print(f'\nResultado: {resultado}')
print('Continuamos...')