ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Continuar ? '))
    if r in 'Nn':
        break
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Qual aluno ? '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Nota de {ficha[opc][0]} são {ficha[opc][1]}')
print('fim')
