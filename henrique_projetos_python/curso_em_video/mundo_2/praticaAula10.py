nome = str(input('Qual é seu nome: '))
if nome == 'Henrique':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) /2
print('A sua media foi {:.1f}'.format(m))
print('Parabens' if m>=6 else 'Estude mais')
