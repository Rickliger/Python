distancia = float(input('Qual sera a distancia da sua viagem? '))

if distancia <= 200:
    preçoduzentos = distancia * 0.5
    print('A sua viagem com distancia de {} tera o valor de R${:.2f}'.format(distancia, preçoduzentos))
else:
    preçomais = distancia * 0.45
    print('A sua viagem com distancia de {} tera o valor de R${:.2f}'.format(distancia, preçomais))
print('Tenha uma oba viagem')
