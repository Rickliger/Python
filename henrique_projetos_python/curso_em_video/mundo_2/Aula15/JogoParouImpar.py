from random import randint

cont = 0
while True:
    jogador = int(input('Digite um valor ? '))
    computador = randint(0, 11)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar ? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('PAR' if total % 2 == 0 else 'IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu')
            cont += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
            cont += 1
        else:
            print('Voce perdeu')
            break
        print('Vamos de novo')
print(f'Voce perdeu após {cont} vitórias')
