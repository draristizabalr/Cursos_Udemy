import psycopg2 # Librería para poder conectarse a PostgreSQL

conexion = psycopg2.connect(
    user='postgres', # Este es el usuario por defecto de PostgreSQL
    password='admin', # Esta es la contraseña que se dió en el momento de la instalación
    host='127.0.0.1', # Esta es la IP del servidor donde está la base de datos, esta es la IP local
    port='5432', # Este es el puerto que se usa para acceder a los datos de la base de datos, por defecto "5432"
    database='test_db' # Este es el nombre de la base de datos
)

print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # Este objeto es para poder realizar sentencias en PostgreSQL desde Python
            cursor = conexion.cursor()
            # Esta es la sentencia que vamos a realizar en PostgreSQL
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves_primarias = ((1,2,3),)
            entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            # id_persona = input('Proporciona el valor de id_persona: ')
            # Este metodo es para correr la sentencia de PostgreSQL en Python
            cursor.execute(sentencia, llaves_primarias)
            # Guardar los resultados de la sentencia realizada en PostgreSQL
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

