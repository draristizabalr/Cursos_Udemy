from Recursos.Usuario import Usuario
from Recursos.UsuarioDAO import UsuarioDAO

r = None
while r != 5:
    print(
        '''
1) Listar usuarios
2) Agregar usuario
3) Actuazlizar usuario
4) Eliminar usuario
5) Salir
        ''')
    while True:
        try:
            r = int(input('Escoge una opción: '))
            if r < 1 or r > 5:
                print('Error. Opción no válida')
            else:
                break
        except Exception as e:
            print(f'Error en el valor: {e}')
    if r == 1:
        usuarios = UsuarioDAO.seleccion()
        for usuario in usuarios:
            print(usuario)

    elif r == 2:
        username = input('Proporcionar nombre del usuario: ')
        password = input('Proporcionar contraseña del usuario: ')
        usuario = Usuario(username, password)
        UsuarioDAO.insertar(usuario)

    elif r == 3:
        while True:
            try:
                id_usuario = int(input('Proporcionar el Id del usuario que se va a actualizar: '))
                break
            except Exception as e:
                print(f'Error en el valor dado: {e}')
        username = input('Proporcionar nombre del usuario: ')
        password = input('Proporcionar contraseña del usuario: ')
        usuario = Usuario(username, password)
        UsuarioDAO.actualizar(id_usuario, usuario)

    elif r == 4:
        while True:
            try:
                id_usuario = int(input('Proporcionar el Id del usuario que se va a actualizar: '))
                break
            except Exception as e:
                print(f'Error en el valor dado: {e}')
        UsuarioDAO.eliminar(id_usuario)
