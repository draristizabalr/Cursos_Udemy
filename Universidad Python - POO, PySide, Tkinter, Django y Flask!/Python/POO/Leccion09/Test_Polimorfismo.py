from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado1 = Empleado('Juan', 5000)
imprimir_detalles(empleado1)

gerente1 = Gerente('Carlos', 20000, 'Mercadeo')
imprimir_detalles(gerente1)


