n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor '))
s = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
pot = n1 ** n2
print('A soma é {}, \na subtração é {}, \na multiplicação é {}, \na divisão é {:.3f}'.format(s, sub, mult, div))
print('divisão inteira é {}, e a potência é {}'.format(divint, pot))
