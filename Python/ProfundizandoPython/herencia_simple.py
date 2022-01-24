# Ejemplo de herencia simple
class ListaSimple:
    def __init__(self, elementos):
        self.elementos = list(elementos)

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def __getitem__(self, indice):
        return self.elementos[indice]

    def ordenar(self):
        self.elementos.sort()

    def __len__(self):
        return len(self.elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.elementos!r}'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenar de nuevo la lista
        self.ordenar()

class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    # Sobreescribimos el metodo agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)

# Lista Simple
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)

# Lista Ordenada
lista_ordenada = ListaOrdenada([4, 3, 6, 9, 10, -1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))

# Lista Enteros
lista_enteros = ListaEnteros([-15, 1, 4, 3])
print(lista_enteros)