numeros = (int(input(f'Digite o 1º numero : ')),
           int(input(f'Digite o 2º numero : ')),
           int(input(f'Digite o 3º numero : ')),
           int(input(f'Digite o 4º numero : ')),)

print(f'Voce digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na posição {numeros.index(3)}')
else:
    print('O valor 3 nao foi digitado')
print(f'Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
