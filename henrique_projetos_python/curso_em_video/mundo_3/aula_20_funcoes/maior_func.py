def maior(*num):
    cont = maior = 0
    print('\n Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor foi {maior}')


maior(2, 0, 57, 78, 5, 1, 5, 7, )
