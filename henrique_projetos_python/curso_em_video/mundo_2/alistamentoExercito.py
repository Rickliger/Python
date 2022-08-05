from datetime import date
atual = date.today().year
sexo = str(input('''Sexo:
    FEMININO:  digite F
    MASCULINO: digite M
    Sua resposta: ''')).upper()
if sexo == 'F':
    print('Você não precisa se alistar')
else:
    nasc = int(input('Em que ano voce nasceu? '))
    idade = atual - nasc

    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if sexo == 'M' and idade == 18:
    print('Já está no momento de voce se alistar.')
elif sexo == 'M' and idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos até voce se alistar'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif sexo == 'M' and idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Voce ja deveria ter se alistado a {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
