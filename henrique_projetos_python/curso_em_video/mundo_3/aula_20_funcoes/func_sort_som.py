from random import randint

numbers = list()
pares = list()


def sorteia():
    for c in range(1, 5):
        num = randint(0, 9)
        numbers.append(num)
    print(f'Os numeros sorteados foram {numbers}')


def somaPar():

    total = 0
    for n in numbers:
        if n % 2 == 0:
            pares.append(n)
            total += n
    print(f'Os numeros pares foram {pares}')
    print(f'O total da soma dos numeros pares foi {total}')


sorteia()
somaPar()
