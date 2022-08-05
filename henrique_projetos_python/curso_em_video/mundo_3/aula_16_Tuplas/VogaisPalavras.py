palavras = ('aprender', 'programar', 'linguagem',
          'python', 'curso', 'gratis', 'estudar',
          'praticar', 'trabalhar', 'mercado',
          'programador', 'futuro', 'combustivel')

for p in palavras:
    print(f'\nNa palavra \033[1;32;40m{p.upper()}\033[0;;m temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')