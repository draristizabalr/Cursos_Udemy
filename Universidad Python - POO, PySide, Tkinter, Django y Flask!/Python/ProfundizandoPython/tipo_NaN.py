# NaN significa que no es un numero.
# No es sensible a mayúsculas o minúsculas
# Es un tipo numerico que no está definido
import math as mt
from decimal import Decimal

# Math
a = float('NaN')
print(f'a: {a}')
print(f'Es NaN (Not a number)?: {mt.isnan(a)}')

# Decimal
a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (Not a number): {mt.isnan(a)}')
