total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total foi R$ {total:.2f}')
print(f'E teve {totmil} produtos acima de R$ 1000.00')
print(f'O produto mais barato foi {barato} e custou R$ {menor:.2f}')
