import psycopg2 # Librería para poder conectarse a PostgreSQL

conexion = psycopg2.connect(user='postgres', password='admin',host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Arturo', 'Cardenas', 'acardenas@mail.com', 1),
                       ('Elisabeth', 'Jaramillo', 'ejaramillo@mail.com', 2),
                        )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
            del sentencia, valores
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Camila', 'Bedoya', 'cbedoya@mail.com')
            cursor.execute(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()