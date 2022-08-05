'''cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))

hip = (cat_op ** 2 + cat_adj ** 2) ** (1/2)

print('O cat. opost. é {} e o cat. adj. é {}, então sua hipotenusa é {.:2f}.'.format(cat_op, cat_adj, hip))'''

from math import hypot
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(cat_op, cat_adj)
print('O valor da hipotenusa é de {:.2f}.'.format(hip))
