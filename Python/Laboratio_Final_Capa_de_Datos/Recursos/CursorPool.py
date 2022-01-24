from Conexion import Conexion
from logger_base import log

class CursorPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        log.debug(f'Cursor creado: {self._cursor}')
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_excepcion):
        log.debug('Cerrando bloque with.')
        if valor_excepcion:
            self._conexion.rollback
            log.error(f'Error en la conexión: {valor_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Se guardaron los datos en el database.')
        self._cursor.close
        Conexion.liberarPool

if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute()



