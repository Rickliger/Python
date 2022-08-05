def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)

            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)

            cont -= p
        print('Fim!')


contador(10, 20, 2)
contador(100, 20, 10)
i = int(input('Digite o inicio: '))
f = int(input('Digite o final: '))
p = int(input('Digite os passos: '))
contador(i, f, p)
