# Profundizando en los diferentes sistemas de numeración

# Decimal
decimal = 10
print(f'Decimal: {decimal}')
# Binario: se comienzan los numeros con los caracteres "0b" (0,1)
binario = 0b1010
print(f'Binario: {binario}')
# Octal: se comienzan los numeros con los caracteres "0o" (0,1,2,3,4,5,6,7)
octal = 0o12
print(f'Octal: {octal}')
# Hexadecimal: se comienzan los con los caracteres "0x" (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)
hexadecimal = 0xA
print(f'Hexadecimal: {hexadecimal}')

# Convertir un numero entero, incluyendo su base
print('Convertir numeros de los diferentes sistemas'.center(70,'-'))
# Decimal
decimal = int('23', 10) # Por default es base 10
print(f'Decimal: {decimal}')
# Binario
binario = int('10111', 2)
print(f'Binario: {binario}')
# Octal
octal = int('27', 8)
print(f'Octal: {octal}')
# Hexadecimal
hexadecimal = int('17', 16)
print(f'Hexadecimal: {hexadecimal}')
# Base 5, no es muy común
base5 = int('43', 5)
print(f'Base 5: {base5}')

