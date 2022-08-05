altura = float(input('Qual a sua altura ? '))
peso = float(input('Qual o seu peso (KG)? '))

imc = peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f} e está '.format(imc), end = '')

if imc < 18.5:
    print('abaixo do peso.')
elif 18.5 <= imc < 25:
    print('no peso ideal.')
elif 25 <= imc < 30:
    print('com sobrepeso.')
elif 30 <= imc < 40:
    print('obesa.')
else:
    print('com obesidade morbida, cuidado!')
