# Manejo de valores infinitos
import math as mt
from decimal import Decimal

infinito_positivo = float('inf')
print(f'Infinito positivo: {infinito_positivo}')
print(f'¿Es infinito? {mt.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')
print(f'¿Es infinito? {mt.isinf(infinito_negativo)}')

# Modulo math
infinito_positivo = mt.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'¿Es infinito? {mt.isinf(infinito_positivo)}')

infinito_negativo = -mt.inf
print(f'Infinito negativo: {infinito_negativo}')
print(f'¿Es infinito? {mt.isinf(infinito_negativo)}')

# Modulo Decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'¿Es infinito? {mt.isinf(infinito_positivo)}')

infinito_negativo = -Decimal('Infinity')
print(f'Infinito negativo: {infinito_negativo}')
print(f'¿Es infinito? {mt.isinf(infinito_negativo)}')