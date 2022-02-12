import psycopg2 as db

class Conexion:

    DATABASE = 'persona'
    USERNAME = 'postgres'
    PASSWORD = 'admin'
    HOST = '127.0.0.1'
    DB_PORT = '5432'
    conexion = dc.connect(user=Conexion.USERNAME, password=Conexion.PASSWORD, host=Conexion.HOST, port=Conexion.DB_PORT, )

    def __init__(self, database):
        self._database = database

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, database):
        self._database = database

    def __str__(self):
        if self._accion == 1:
            return f'SELECT * FROM {self._database}'
        elif self._accion == 2:
            return f'INSERT INTO {self._database}'
        elif self._accion == 3:
            return f'UPDATE {self._database} SET '
        elif self._accion == 4:
            return f'DELETE FROM {self._database} '

    def sentencia(self):
        return ClasePostgreSQL.__str__()
