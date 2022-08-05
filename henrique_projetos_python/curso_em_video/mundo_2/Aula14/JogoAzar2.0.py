from random import randint
maquina = randint(0, 10)
acertou = False
cont = 0
print('Vou pensar em um numero tente advinhar')
while not acertou:
    jogador = int(input('Em que numero eu pensei? '))
    cont += 1
    if jogador == maquina:
            acertou = True
    else:
        if jogador < maquina:
            print('Mais... tente novamente.')
        elif jogador > maquina:
            print('Menos... tente novamente.')
print('Parabens voce acertou! Após {} tentativas!'.format(cont))
