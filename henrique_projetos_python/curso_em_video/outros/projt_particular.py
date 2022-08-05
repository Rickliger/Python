#Calculo de porcentagem de custo do produto
venda = float(input('Digite o valor que o produto foi vendido: '))

porct = 100 * 30/100

custo = venda - porct

venda = custo + porct

lucro = venda - custo

print('O valor de custo do produto é de {} e o lucro é de {}'.format(custo, lucro))
