from CursorPool import CursorPool
from Usuario import Usuario
from logger_base import log

class UsuarioDAO:

    _SELECCION = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccion(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCION)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = (registro[0], registro[1], registro[2])
                personas.append(persona)
            log.debug('Se mandó a listar la database')
            return personas

    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Nuevos datos: {usuario.informacion()}')

    @classmethod
    def actualizar(cls, id_usuario, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password, id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Valores que se han actualizado: {usuario.informacion()}')

    @classmethod
    def eliminar(cls, id_usuario):
        with CursorPool() as cursor:
            valores = (id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Id del usuario eliminado: {id_usuario}')

if __name__ == '__main__':
    usuario1 = Usuario('pfar6', 1023)
    print(usuario1)

    # SELECT
    usuarios = UsuarioDAO.seleccion()
    for usuario in usuarios:
        log.debug(usuario)

    # INSERT
    UsuarioDAO.insertar(usuario1)

    # UPDATE
    usuario2 = Usuario('drar', 3721)
    UsuarioDAO.actualizar(2, usuario2)

    #DELETE
    UsuarioDAO.eliminar(1)