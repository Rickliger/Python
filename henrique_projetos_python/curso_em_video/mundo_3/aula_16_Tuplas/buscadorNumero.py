cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito',
            'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
            'Dezesete', 'Dezoite', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente de novo', end='')
print(f'Voce digitou o numero {cont[num]}')
