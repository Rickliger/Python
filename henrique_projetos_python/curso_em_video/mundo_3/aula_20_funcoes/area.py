def area(l, c):
    """
    -> Faz um calculo da area de acordo a largura e comprimento
    :param l: largura da area
    :param c: comprimento da area
    """
    print('-' * 10)
    a = l * c
    print(f'As dimensões de {l} x {c} tem Area = {a}m²')


l = float(input('Largura: '))
c = float(input('Altura: '))
area(l, c)

help(area)
