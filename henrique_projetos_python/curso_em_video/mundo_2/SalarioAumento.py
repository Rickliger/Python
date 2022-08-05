salario = float(input('Qual o salario do funcionario? R$ '))

if salario >= 1250:
    salarionv = salario + (salario * 10 / 100)
    print('O salario com o aumento de 10% será R$ {:.2f}'.format(salarionv))
else:
    salarionv = salario + (salario * 15/100)
    print('O salario com o aumento de 15% será R$ {:.2f}'.format(salarionv))
