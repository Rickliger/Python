preçoat = float(input('Quanto custa o produto ? R$ '))
desconto = float(input('Qual o desconto que será aplicado? '))


preçonv = preçoat - (preçoat * desconto/100)

print('O preço do produto com desconte é de R$ {:.2f}.'.format(preçonv))
