lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Este numero ja esta na lista')
    r = str(input('Quer continuar ? '))
    if r in 'nN':
        break
print('-+'*30)
lista.sort()
print(f'Voce digitou os numeros {lista}.')
