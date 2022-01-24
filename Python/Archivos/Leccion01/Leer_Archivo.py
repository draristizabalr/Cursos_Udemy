# Si no se tiene el archivo en la misma carpeta se debe especificar la ruta
archivo = open('c:\\David\\Programas\\Curso_Udemy\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')

# Si se tiene el archivo en la misma carpeta NO se debe especificar la ruta
archivo = open('prueba.txt', 'r', encoding='utf8')

# Para leer el archivo por completo se usa este metodo

# print(archivo.read())

# Leer algunos caracteres

# print(archivo.read(5))
# print((archivo.read(3)))

# Leer lineas completas

# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo
# for line in archivo:
#     print(line)

#leer lineas
# print(archivo.readlines())
# print(archivo.readlines()[0])

# abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()