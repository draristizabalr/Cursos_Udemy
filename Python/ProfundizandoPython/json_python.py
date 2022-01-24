# Leer archivo json
# JSON = Javascript Object Notation
import json
import urllib.request

url = 'http://globalmentoring.com.mx/api/personas.json'
r = urllib.request.Request(url)
r.add_header('User-Agent', 'Mozilla/5.0 (Windows 10; Ryzen 3600')
respuesta = urllib.request.urlopen(r)
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)
# Procesamos la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)                       # Visualizar información JSON
print(type(json_respuesta))                 # Tipo del resultado de leer JSON en Python
print(json_respuesta.keys())                # Sabiendo que es un diccionario, en este caso, saber los keys
print(type(json_respuesta['personas']))     # Tipo de variable que está asociado a la key 'personas'
print(len(json_respuesta['personas']))      # Al saber que es una lista, buscamos que longitud tiene
print(type(json_respuesta['personas'][0]))  # Tipo de variable de los elementos de la lista a la que está asociado
print(json_respuesta['personas'][0].keys()) # Al saber que son diccionarios, buscamos las keys
# Imprimir solo los nombres de las personas
# JSON se convierte en listas o diccionarios en Python
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} - {persona["edad"]}')
# Accedemos a la variable de total
print(f'Total de personas: {json_respuesta["total"]}')
# Accedemos a la variable de mensaje
print(f'Mensaje final del archivo: {json_respuesta["mensaje"]}')
