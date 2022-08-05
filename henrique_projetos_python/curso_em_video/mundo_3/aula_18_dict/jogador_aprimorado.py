time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Continuar ? ')).upper()[0]
        if r in 'SN':
            break
        print('Erro')
    if r == 'N':
        break

print('cod', end='')
for i in jogador.keys():
    print(f'{i:15}',end='')
print()

for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

while True:
    busca = int(input('Mostrar resultados de qual jogador ? '))
    if busca == 999:
        break
    if busca >=len(time):
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f' Levatamento jodador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
print('Final')