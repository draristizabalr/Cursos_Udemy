def celsius_fahrenheit(celsius):
    resultado = celsius * 9/5 + 32
    return resultado

def fahrenheit_celsius(fahrenheit):
    resultado = (fahrenheit-32) * 5/9
    return resultado

celsius = float(input('Proporcionar grados celsius:'))
fahrenheit = float(input('Proporcionar grados fahrenheit: '))
print(f'{celsius}°C es igual a {celsius_fahrenheit(celsius)}°F')
print(f'{fahrenheit}°F es igual a {fahrenheit_celsius(fahrenheit)}°C')