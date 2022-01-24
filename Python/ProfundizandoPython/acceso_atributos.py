# Ejemplo atributos públicos, protegidos y privados

class Mi_clase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

objeto = Mi_clase('Valor público', 'Valor protegido', 'Valor privado')
# Acceso al atributo público
print(objeto.publico)
# Modificar el valor público
objeto.publico = 'Nuevo valor público'
print(objeto.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clases hijas
print(objeto._protegido)
# Modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)

# Acceso al valor privado
# print((objeto.__privado))
# No se puede acceder de forma directa, pero si se puede acceder de la siguiente forma
print(objeto._Mi_clase__privado)
# Modificar el valor privado
objeto._Mi_clase__privado = 'Nuevo valor privado'
print(objeto._Mi_clase__privado)