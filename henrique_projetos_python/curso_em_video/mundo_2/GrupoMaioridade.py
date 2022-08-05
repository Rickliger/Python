from datetime import date

maior = 0
menor = 0
ano = date.today().year
gente_pequena = ''
gente_grande = ''
existe = ''

for c in range(1, 8):
    nasc = int(input('Ano de nasc da {}ª pessoa: '.format(c)))
    idade = ano - nasc
    if idade < 18:
        menor += 1
    elif idade > 18:
        maior += 1
    if menor <= 1:
        existe = 'Existe'
        gente_pequena = 'menor'
    elif menor > 1:
        gente_pequena = 'menores'
    elif maior <= 1:
        gente_grande = 'maior'
    elif maior > 1:
        gente_grande = 'maiores'
'''if menor > 1 and maior > 1:
    existe = 'Existem'
    gente_pequena = 'menores'
    gente_grande = 'maiores'
elif menor == 1 and maior == 1:
    existe = 'Existe'
    gente_pequena = 'menor'
    gente_grande = 'maior'
elif menor > 1 and maior == 1:
    existe = 'Existem'
    gente_pequena = 'menores'
    gente_grande = 'maiores'
elif menor == 1 and maior > 1:
    existe = 'Existe'
    gente_pequena = 'menor'
    gente_grande = 'maiores' '''

print('{} {} {} de idade e {} {} de idade.'.format(existe, menor, gente_pequena, maior, gente_grande))
