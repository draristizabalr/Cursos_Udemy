def calcular_total(pago_sin_impuesto, impuesto):
    resultado = pago_sin_impuesto * (1+(impuesto/100))
    return resultado

pago_sin_impuesto = float(input('Proporcionar pago sin el impuesto: '))
impuesto = float(input('Proporcionar el porcentaje del impuesto: '))
print(f'El pago con impuestos es: ${calcular_total(pago_sin_impuesto,impuesto)}')
