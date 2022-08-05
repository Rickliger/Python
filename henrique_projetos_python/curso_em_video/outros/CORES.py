nome = 'Henrique'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarela':'\033[33m',
         'pretoebranco':'\033[7;30'}
print('Ola {}{}{}'.format(cores['amarela'], nome, cores['limpa']))
