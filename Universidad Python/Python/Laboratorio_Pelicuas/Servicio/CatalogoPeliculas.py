import os

class CatalogoPeliculas:
    nombre_catalago = 'catalogo_peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.nombre_catalago, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.nombre_catalago, 'r', encoding='utf8') as archivo:
            print('Catalogo de peliculas '.center(50,'-'))
            for line in archivo:
                print(line)

    @classmethod
    def eliminar_peliculas(cls):
        try:
            os.remove(cls.nombre_catalago)
            print(f'Archivo eliminado: {cls.nombre_catalago}')
        except Exception:
            print('No se ha creado un catalogo aún.')