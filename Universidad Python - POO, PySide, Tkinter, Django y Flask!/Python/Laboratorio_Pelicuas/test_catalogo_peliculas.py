from dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas as CP

def opciones():
    while True:
        print('-' * 50)
        try:
            r = int(input('Escribe tu opción: '))
            if r < 1 or r > 4:
                print('Opción no valida.')
            else:
                break
        except ValueError:
            print('Valor no válido.')

    return str(r)

respuesta = None

while respuesta != '4':
    print('1) Agregar pelicula\n2) Listar peliculas\n3) Eliminar catalogo\n4) Salir\n')
    respuesta = opciones()
    if respuesta == '1':
        print('-' * 50)
        pelicula = input('Proporcionar la película: ')
        CP.agregar_pelicula(Pelicula(pelicula))
        print('-' * 50)

    elif respuesta == '2':
        CP.listar_peliculas()
        print('-' * 50)

    elif respuesta == '3':
        CP.eliminar_peliculas()
        print('-' * 50)
        continue

    else:
        break