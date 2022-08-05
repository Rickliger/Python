lista = []
for c in range(0, 5):
    n = int(input(f'Digite o {c}º valor: '))
    if c == 0 or n > lista[- 1]:
        lista.append(n)
        print(f'O valor foi adicionado ao final da lista.')
    # Busca o ultimo valor('len' = tamanho) - 1 traz o ultimo valor
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}.')
                # Na posição 'pos' o numero 'n'
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
