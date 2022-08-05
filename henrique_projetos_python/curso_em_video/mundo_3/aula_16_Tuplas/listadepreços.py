lista = ('Lapis', 1.53,
         'Borracha', 2,
         'Caderno', 12.4,
         'Estojo', 4,
         'Transferidor', 2.3,
         'Compasso', 9.99,
         'Mochila', 40,
         'Canetas', 22.30,
         'Livro', 32.98)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'\033[1;34;40m {lista[pos]: <20}\033[0;30;m', end='' )
    else:
        print(f'\033[0;32;40m R$ {lista[pos]:>.2f} \033[0;30;m')
