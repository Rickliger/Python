lista = []
menor = 0
maior = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]

print(f'Voce digitou os numeros {lista}')
print(f'O maior valor dentro dessa lista foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}; ', end='')
print(f'\nO menor valor dentro dessa lista foi {menor} nas posições', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}; ', end='')
print('Fim do programa')
