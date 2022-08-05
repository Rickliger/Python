'''r = 'S'''
'''while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]')).upper()
print('Fim)'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 12
print('Voce digitou {} numeros pares e {} numeros impares'.format(par, impar))
