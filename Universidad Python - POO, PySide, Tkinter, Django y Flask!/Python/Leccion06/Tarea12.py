def count_down(numero):
    if numero < 1:
        return ''
    else:
        print(numero)
        return count_down(numero-1)

print(count_down(-1))