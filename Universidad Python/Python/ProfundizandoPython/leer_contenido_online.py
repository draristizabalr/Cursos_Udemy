# Leer el contenido online
from urllib.request import urlopen, Request

palabras = []
with urlopen(Request('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
             headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0)'
             'Gecko/20100101 Firefox/78.0'})) as mensaje:

    contenido = mensaje.read().decode('UTF-8')

# Contar palabras
print('No. que aparece la palabra universidad:', contenido.count('Universidad'))
print(contenido.upper())
print(contenido.lower())

# Buscamos la cadena 'python' en el contenido
print('¿Existe python?', 'python'.lower() in contenido.lower())
print('¿Existe python?', 'python'.upper() in contenido.upper())

# startswith - inicia con cierto str y endswith - finaliza con cierto str
print('Inicia con:', contenido.startswith('En GlobalMentoring.com.mx'))
print('Termina con:', contenido.lower().endswith('GlobalMentoring.com.mx'.lower()))

#     print(contenido)
#
# with open('nuevo_archivo.txt', 'w', encoding='UTF-8') as archivo:
#     for line in contenido:
#         archivo.write(line)