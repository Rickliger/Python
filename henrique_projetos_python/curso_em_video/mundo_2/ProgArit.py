init = int(input('Por qual o valor deseja começar ? '))
razão = int(input('A cada quantos passos ? '))
decimo = init + (10 - 1) * razão
for c in range(init, decimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('Fim')
