s = 0
cont = 0
for c in range(1, 904, 1):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma total dos {} valores é {}'.format(cont, s))
