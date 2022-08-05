lista = []
r = ''
c = 0
while True:
    lista.append(int(input('Digite um numero: ')))
    c += 1
    r = str(input('Quer continuar [s/n]? '))
    if r in 'Nn':
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Ordenados descrescentemente {lista}')
if 5 in lista:
    print('O nº 5 faz parte da lista.')
else:
    print('O nº 5 não foi encontrado na lista!')
