#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias o carro foi alugado? '))

km = float(input('Quantos Km foram rodados com o carro? '))

alug_d = dias * 60

alug_km = km * 0.15

total = alug_d + alug_km

print('Seu carro foi alugado por {} dias e rodou {} km nesse periodo. Com base nisso seu custo total será de R$ {:.2f}'.format(dias, km, total))
