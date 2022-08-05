'''from time import sleep
n = n2 = 0
r = 0
s = 0
while r == '':
    n = float(input('Digite o {}º valor: ').format(r))
    r = int(input('Qual operação deseja fazer ?
    [1] somar
    [2] multiplicar
    [3] novos numeros
    [5] sair do programa'))
    if r == 1:
        s = n + n2
    elif r == 2:
        s = n * n2
    elif r == 3:
        n2 = float(input('Digite o {}º valor: ').format(r))
    elif r == 5:
        sleep(1)
        print('Encerrando o programa')'''
from time import sleep
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
opção = 0

while opção != 5:
    print('''[1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do prograna ''')
    opção = int(input('Qual opção ? '))
    if opção == 1:
        soma  = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Encerrando o programa')
        sleep(2)
    else:
        print('Opção invalida. Tente novamente.')
print('Encerrando')
