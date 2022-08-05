from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento ? '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('A sua categoria é mirim')
elif idade <= 14:
    print('Sua categoria é infantil')
elif idade <= 19:
    print('Sua categoria é junior')
elif idade <= 25:
    print('Sua categoria é senior')
else:
    print('Sua categoria é master')
