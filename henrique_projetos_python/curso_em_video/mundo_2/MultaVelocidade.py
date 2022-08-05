velocidade = float(input('A qual velocidade o carro passou? '))

if velocidade > 80:
    print('MULTADO! Voce excedeu o limite de velocidade, que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
