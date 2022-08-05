from time import sleep
from random import randint
maquina = randint(0, 5)
#print('Pensei no numero {}'.format(maquina))
print('--'*20)
print('Vou pensar em numero tente adivinhar.')
print('--'*20)
sleep(1)
jogador = int(input('Em que numero eu pensei? '))

if jogador == maquina:
    print('Parabens voce ganhou')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}!'.format(maquina, jogador))
