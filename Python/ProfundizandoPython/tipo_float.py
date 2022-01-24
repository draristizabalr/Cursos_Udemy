# Profundizando en el tipo float
a = 3.0
print(f'a: {a:.2f}')
# En el momento que agregamos dos al momento de imprimir se le estará indicando el formato
# . - Para indicar la cantidad de decimales
# f - Para indicar que es de puntoflotante, antes se debe indicar la cantidad de decimales a mostrar

# Constructor de tipo flotante
a = float('10')
print(f'a: {a:.2f}')

#Notacion exponencia, en valores positivos o negativos
exponencialp = 3e5
print(f'Exponencial positivo: {exponencialp:.2f}')
exponencialn = 3e-5
print(f'Exponencial negativo: {exponencialn:.6f}')

# En el momento que se opere con una variable tipo float el resultado se combertirá en tipo flotante
resultado = 4.0 + 5
print(f'Tipo de variable 4.0: {type(4.0)}')
print(f'Tipo de variable 5: {type(5)}')
print(f'Tipo de variable 4.0 + 5: {type(resultado)}')

