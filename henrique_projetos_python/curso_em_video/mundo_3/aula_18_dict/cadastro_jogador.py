jogador = dict()
partida = list()
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for c in range(0, tot):
    partida.append(int(input(f'Gols na {c+1}ª partida: ')))
jogador['gols'] = partida[:] #'[:]' cria uma cópia da lista
jogador['total'] = sum(partida)
print(jogador)

for k, v in jogador.items():
    print(f'O campo {k} corresponde á {v}')

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
