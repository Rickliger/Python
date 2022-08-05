galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Continuar [S/N] ? ')).upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print(f'{len(galera)} cadastros')
media = soma / len(galera)
print(f'Média de idade: {media:5.2f} anos.')
print(f'Mulheres cadastradas', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(f'Pessoas acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('fim :(')
