from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado
from mundo_pc.Monitor import Monitor
from mundo_pc.Computador import Computador
from mundo_pc.Orden import Orden

# Creación de los objetos "Raton"
raton1 = Raton('HP', 'USB')
raton2 = Raton('ACER', 'bluetooth')
raton3 = Raton('gamer', 'bluetooth')

# Creación de los objetos "Teclado"
teclado1 = Teclado('HP', 'USB')
teclado2 = Teclado('ACER', 'bluetooth')
teclado3 = Teclado('Gamer', 'bluetooth')

# Creación de los objetos "Monitor"
monitor1 = Monitor('HP', 15)
monitor2 = Monitor('ACER', 27)
monitor3 = Monitor('Gamer', 45)

# Creación de los objetos "Computador"
computador1 = Computador('HP', monitor1, teclado1, raton1)
computador2 = Computador('ACER', monitor2, teclado2, raton2)
computador3 = Computador('Gamer', monitor3, teclado3, raton3)


#Creación de las ordenes
pedido1 = [computador1, computador2]
pedido2 = [computador3, computador1]

orden1 = Orden(pedido1)
orden2 = Orden(pedido2)

print(orden1, orden2, sep='\n')







