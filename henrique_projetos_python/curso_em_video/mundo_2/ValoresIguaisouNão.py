n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O {} é o maior valor'.format(n1))
elif n2 > n1:
    print('O {} é o maior valor'.format(n2))
else:
    print('Os dois valores são iguais.')
