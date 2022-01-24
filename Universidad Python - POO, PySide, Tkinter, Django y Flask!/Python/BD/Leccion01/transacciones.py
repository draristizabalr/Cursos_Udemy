import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin',host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores = ('Olga Carmenza', 'Ramírez', 'ocramirez@qmail.com')
            cursor.execute(sentencia,valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Jaime Alfonso', 'Aristizábal', 'jaaristizabal@mail.com', 1)
            cursor.execute(sentencia,valores)
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

print('Termina la transacción, se hizo commit')

