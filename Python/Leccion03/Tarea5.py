calificacion = float(input('Proporcionar un valor entre 0  y 10: '))
if calificacion <= 10 and calificacion >= 9:
    print('A')
elif calificacion < 9 and calificacion >= 8:
    print('B')
elif calificacion < 8 and calificacion >= 7:
    print('C')
elif calificacion < 7 and calificacion >= 6:
    print('D')
elif calificacion < 6 and calificacion >= 0:
    print('F')
else:
    print('Calificación no valida.')