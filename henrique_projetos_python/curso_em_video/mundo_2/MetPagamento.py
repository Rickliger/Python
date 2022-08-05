print('{:=^40}'.format(' HL STORE '))

preço = float(input('Qual o valor total ? R$ '))

print('--'*20)
print('''Metodos de pagamento.
(1)A vista (10% de desc.)
(2)A vista no cartao (5% de desc.)
(3)2x no cartao (preço normal)
(4)3x ou mais no cartao (20% de juros)''')
print('--'*20)

met_pag = int(input('''Digite uma das opções (1) (2) (3) (4) 
    Sua opção: '''))

if met_pag == 1:
    total = preço - (preço*10/100)
    print('Voce recebeu 10% de desc. e o seu produto custara R$ {:.2f}'.format(total))
elif met_pag == 2:
    total = preço - (preço*5/100)
    print('Voce recebeu 5% de desc. e o seu produto custara R$ {:.2f}'.format(total))
elif met_pag == 3:
    totparc = preço/2
    print('Voce parcelou a sua compra em 2x com o valor de {:.2f} cada parcela'.format(totparc))
elif met_pag == 4:
    total = preço + (preço*20/100)
    totparc = int(input('Quantas parcelas ? '))
    parc = total / totparc
    print('Sua compra de R$ {:.2f} parcelada em {}x custará R$ {:.2f} cada parcela com um total de R$ {:.2f}'.format(preço, totparc, parc, total))
