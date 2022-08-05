s = 0
for c in range(0, 6):
    n = int(input('Digite um numero inteiro: '))
    if c % 2 == 0:
        s = s + n
print('O somatorio total de todos os valores foi {}'.format(s))
