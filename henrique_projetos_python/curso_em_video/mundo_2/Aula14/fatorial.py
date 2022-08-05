n = int(input('Digite o numero para o fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
    f *= c
print('o fatorial de {} teve um total de {}'.format(n, f))
