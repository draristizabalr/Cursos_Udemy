import json
import urllib.request

# Creamos una variable con la url del archivo JSON que vamos a trabajar
url = 'http://globalmentoring.com.mx/api/clima.json'

# Creamos un objeto Request, para agregar detalles en la conexión y así no generarse el error 406
r = urllib.request.Request(url)

# Agregamos los headers a nuestro objeto r donde le especificamos el navegador (se usa Mozilla porque es el que
# tiene mayor compatibilidad), el sistema operativo, el procesador del computador y se pueden especificar otros
# datos si es necesario, como: la versión del navegador, version Geko y algunas otras cosas más
r.add_header('User-Agent', 'Mozilla/5.0 (Windows 10; Ryzen 3600')

# Ya con nuestro objeto r bien definido procedemos a abrir la url
respuesta = urllib.request.urlopen(r)

# Se leen los datos del resultado de entrar en la url
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)

# Decodificamos y organizamos la información recibida del JSON
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)

# Ahora ya debidamente organizados los datos, vamos a encontrar: la Descripción, temperatura máxima y mínima
# Primero miramos que tipo de variable es en general
print(type(json_respuesta))

# Al saber que es un diccionario vamos a ver cuáles son las llaves de diccionario
print(json_respuesta.keys())

# Encontramos la llave de 'clima' que es en donde está nuestro primer dato a buscar "descripcion"
# Verificamos que tipo de variable alberga la llave 'clima'
print(type(json_respuesta['clima']))
print(len(json_respuesta['clima']))

# Al ver que es una lista de un solo elemento entramos en este y mandamos a llamar la llave 'descripcion'
print(f'El valor de la descripción en el archivo JSON es: {json_respuesta["clima"][0]["descripcion"]}')

# Ahora vamos a encontrar los datos de temperatura máxima y mínima que están en la llave 'principal'
# Primero verificamos que tipo de variable contiene la llave 'principal
print(type(json_respuesta['principal']))

# Encontramos que la llave principal está asociada a un diccionario, entonces encontraremos las llave de este
print(json_respuesta['principal'].keys())

# Hallamos las llaves de temp_min (temperatura mínima) y temp_max (temperatura máxima) que son los datos que
# necesitamos. Los mandamos a llamar para dar nuestro resultado
print(f'El valor de la descripción en el archivo JSON es: {json_respuesta["clima"][0]["descripcion"]}')
print(f'La temperatura máxima es: {json_respuesta["principal"]["temp_max"]}')
print(f'La temperatura mínima es: {json_respuesta["principal"]["temp_min"]}')

