import psycopg2 # Librería para poder conectarse a PostgreSQL

conexion = psycopg2.connect(user='postgres', password='admin',host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los "id_persona" que quieras eliminar (separados por comas ","): ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
finally:
    conexion.close()