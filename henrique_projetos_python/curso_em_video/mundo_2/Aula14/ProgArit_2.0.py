primeiro = int(input('1º termo: '))
razao = int(input('Razao PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
