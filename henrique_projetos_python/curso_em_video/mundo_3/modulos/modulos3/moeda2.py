def aumentar2(preco=0, taxa=0):
    res = preco + (preco * taxa / 100)
    return res


def diminuir2(preco=0, taxa=0):
    res = preco - (preco * taxa / 100)
    return res


def dobro2(preco=0):
    res = preco * 2


def metade2(preco=0):
    res = preco / 2


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
