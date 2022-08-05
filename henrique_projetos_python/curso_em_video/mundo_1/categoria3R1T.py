r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos formam um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r3:
        print('ESCALENO')
    else:
        print('ISOCELES.')
else:
    print('Nao formam um triangulo')
