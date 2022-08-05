primeiro = int(input('1º: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer a mais ? '))
print('FIM')
