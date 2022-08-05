casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário: R$ '))
tempo = int(input('Quanto anos de financiamento ? '))

prestação = tempo*12
valprestação = casa / prestação
minimo = salario*30/100

if valprestação >= minimo:
    print('Não aprovado! '
          'O valor da prestação excede 30% do seu salário!')
else:
    print('Parabens! Seu emprestimo foi aprovado!')
    print('O valor da prestação será de {:.2f} '
      'e será quitado em {} meses.'.format(minimo, prestação))
