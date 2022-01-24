from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    @property
    def id_orden(self):
        return self._id_orden

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, productos):
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self.productos:
            productos_str += producto.__str__() + '|'
        return f'Orden {self.id_orden}:\nProductos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)
    productos = [producto1, producto2]
    orden1 = Orden(productos)
    print(orden1)
