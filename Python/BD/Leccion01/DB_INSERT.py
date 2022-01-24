import psycopg2 # Librería para poder conectarse a PostgreSQL

conexion = psycopg2.connect(user='postgres', password='admin',host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (('Daniel', 'Botero', 'dbotero@mail.com'),
                       ('Jose Mateo', 'Aristizábal', 'jmaristizabal@mail.com'),
                       ('Juan Sebastián', 'Macias', 'jsmacias@mail.com'),)
            cursor.executemany(sentencia, valores)
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()