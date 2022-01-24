# Profundizar en el usa de set
# Una colección de elementos únicos y es mutable
# Los elementos de un set son inmutables
conjunto = {'Juan', True, 18.0}
print(conjunto)

# Set vacio
conjunto = {}
print(type(conjunto))
conjunto = set()
print(conjunto)
print(type(conjunto))

# Mutable
conjunto.add('Juan')
print(conjunto)

# Contiene valores únicos
conjunto.add('Juan')
print(conjunto)

# Crear un set con un iterable
conjunto = set([4, 5, 6, 7, 8, 4])
print(conjunto)

# Podemos agregar más elementos o incluso otro set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20, 30, 40, 50])
print(conjunto)

# Copiar un set (copia poco profunda, solo copia referencias
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar la igualdad de los dos set
print(f'¿Es igual en contenido? {conjunto == conjunto_copia}')
print(f'¿Es la misma referencia? {conjunto is conjunto_copia}')

# Operaciones en conjuntos con set
# Personas con distintas caracteristicas
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}
# Todos con ojos_cafe o pelo_rubio (Union) (no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado
print(pelo_rubio.union(ojos_cafe))

# Intersection Solo las personas con ojos_cafe y pelo_rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# Difference pelo_negro pero sin ojos_cafe
print(pelo_negro.difference(ojos_cafe))

# Diferencia simetrica pelo_negro u ojos_cafe, pero NO ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# Preguntar si un set está contenido en otro conjunto
print(menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set
# Preguntar si los elementos de un set están contenidos en otro set
print(menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo_negro no tiene el pelo_rubio (distjoint)
print(pelo_negro.isdisjoint(pelo_rubio))


