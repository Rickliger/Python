import moeda2

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.diminuir2(p))}')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.diminuir2(p))}')
print(f'Aumentando 10%, temos {moeda2.moeda(moeda2.diminuir2(p, 10))}')
print(f'Diminuido 13%, temos {moeda2.moeda(moeda2.diminuir2(p, 13))}')
