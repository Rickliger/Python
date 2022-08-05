"""def lin():
    print('HELLO MY BITCH')

lin()
print('Hello')"""

"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(b=4, a=1)
soma(4, 2)
soma(1, 2)"""

"""def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('fim')


contador(1, 3, 3, 4, 6)
contador(5, 9)
contador(1, 7)"""


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [4, 6, 7, 1, 7, 8]
dobra(valores)
print(valores)
