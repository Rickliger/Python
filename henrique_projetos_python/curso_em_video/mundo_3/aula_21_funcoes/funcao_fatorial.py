def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero
    :param n: Valor que será calculado o fatorial
    :param show: Escreve o cálculo efetuado na tela.
    :return: O valor faotiral de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(4, show=True))
help(fatorial)