alt = float(input('Qual a altura da area? '))
larg = float(input('Qual a largura da area? '))

area = alt * larg
tinta = area / 2
print('A dimensão da sua área é {}x{} e a área é de {} m².'.format(larg, alt, area))
print('A quantidade de tinta necessária será de {}l.'.format(tinta))
