salarioat = float(input('Qual o salrio atual do funcionário? R$ '))

aumento = float(input('Quantos % será dado de aumento? '))

salarionv = salarioat + (salarioat * aumento/100)

print('O salário atual do funcionário é R$ {:.2f} e com o aumento será R$ {:.2f}.'.format(salarioat, salarionv))
