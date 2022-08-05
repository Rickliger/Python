somaidade = 0
medidaidade = 0
maisvelhohome = 0
nomevelho = ''
totomulher20 = 0
for p in range(1, 5):
    print('{}º Pessoa'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'mM':
        maisvelhohome = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maisvelhohome:
        maisvelhohome = idade
        nomevelho = nome
    if sexo in 'fF' and idade > 20:
        totomulher20 += 1
medidaidade = somaidade/4
print('A media de idade do grupo é de {:.0f} anos'.format(medidaidade))
print('O homem mais velho tem {} e se chama {}'.format(maisvelhohome, nomevelho))
print('Ao todo sao {} mulheres com 20 anos'.format(totomulher20))
