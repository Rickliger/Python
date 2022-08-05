def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero inteiro válido.\033[m')
        if ok:
            break
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
