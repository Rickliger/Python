s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Voce informou {} valores PARES e a soma total foi {}'.format(cont, s))
