def multiplicar(*args):
    mult = 1
    for numero in args:
        mult *= numero
    return mult

print(multiplicar(3,5,15))  