from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _USUARIO = 'postgres'
    _HOST = '127.0.0.1'
    _PASSWORD = 'admin'
    _PORT = '5432'
    _DATABASE = 'test_db'
    _MIN = 1
    _MAX = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN, cls._MAX,
                                                      host=cls._HOST,
                                                      user=cls._USUARIO,
                                                      port=cls._PORT,
                                                      password=cls._PASSWORD,
                                                      database=cls._DATABASE)
                log.debug(f'Se creó el pool exitósamente: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error: {e}')
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión exitosa: {conexion}')
        return conexion

    @classmethod
    def liberarPool(cls):
        cls.obtenerPool().putconn()
        log.debug(f'Se libera el pool: {cls._pool}')


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    print(conexion1)
