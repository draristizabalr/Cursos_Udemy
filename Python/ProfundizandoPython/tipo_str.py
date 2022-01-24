# Profundizando en el tipo str

# Concatenación automatica en Python

variable = 'Adios'
mensaje = 'Hola' 'Mundo' + variable
mensaje += 'Universidad' 'Python'
print(mensaje)

# Recordar que los str son inmutables
# Demostración
print('Demostración'.center(50,'-'))
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'Mensaje 1: {mensaje1}, id: {id(mensaje1)}')
print(f'Mensaje 2: {mensaje2} id: {id(mensaje2)}')
mensaje1 += 'adios'
print(f'Mensaje 1: {mensaje1}, id: {id(mensaje1)}')
# Se puede ver que los ids de cada uno de los mensajes es diferente lo que nos dice que son
# caracteres que redefinen una variable

# Metodo "join"
print('Metodo join'.center(50,'-'))
tupla_str = ('Hola', 'mundo', 'universidad', 'Python')
mensaje = ' '.join(tupla_str)
print(mensaje)

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(mensaje)

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(mensaje)

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(llaves)
print(valores)

# Formato de str con parametros posicionales
print('Formato str'.center(50,'-'))
# % para comenzar el formato:
# s - Para str
# d - Para int
# f - Para float, recordar que primero va ".", después el numero de decimales y después la letra "f"

nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad)
print(mensaje_con_formato)

persona = ('Karla', 'Gomez', 5000.0)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es: %.2f'%persona
print(mensaje_con_formato)
# Esto es igual a:
mensaje_con_formato = 'Hola %s %s. Tu sueldo es: %.2f'
print(mensaje_con_formato%persona)

nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje = 'Sueldo {2:.2f} Edad {1} Nombre {0}'.format(nombre, edad, sueldo)
print(mensaje) # Podemos ver que en este caso, indicamos los indices y ya no import el orden en el que agregamos
               # los datos de la colección

mensaje = 'Sueldo {s:.2f} Edad {e} Nombre {n}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje) # En este caso indicamos los indices con el nombre que querramos y en el momento de agregar los
               # datos debemos de indicar que valor va a cada variable

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]}'.format(dic=diccionario)
print(mensaje) # Aquí renombramos la variable de diccionario y agregamos cada una de las keys del
               # diccionario como indise en el str

# Unicode: se pueden buscar los valores en paginas de internet de cada uno de los caracteres
print('Unicode'.center(50,'-'))

print('Imprimiendo el valor \'A\' en unicode: \u0041')
print('Notación extendida: \U00000041')
print('Notacion hexadecimal: \x41')
print('Corazon: \u2665')
print('Cara sonriendo: \U0001f600')
print('Serpiente: \U0001f40d')

# ASCII: se pueden buscar los valores en paginas de internet de cada uno de los caracteres
print('ASCII'.center(50,'-'))

caracter = chr(65)
print(f'La letra \'A\' es: {caracter}')
caracter = chr(64)
print(f'El \'@\' es: {caracter}')
caracter = chr(97)
print(f'El \'a\' es: {caracter}')

# bytes
print('bytes'.center(50,'-'))
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir de str a bytes
print('Convertir de str a bytes'.center(50,'-'))

string = 'Programación Python'
print(f'string original: {string}')

bytes = string.encode('UTF-8')
print(f'bytes codificado: {bytes}')

# Convertir de bytes a string
string2 = bytes.decode('UTF-8')
print(f'string decodificado: {string2}')
print(string == string2)