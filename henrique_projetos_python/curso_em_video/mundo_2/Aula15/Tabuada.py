while True:

    n = int(input('Digite o numero: '))
    if n < 0:
        for c in range(1, 11):
            print(f'{n} X {c} = {c*n}')
    else:
        print('Numero invalido')
        break
print('Fim do Programa')
