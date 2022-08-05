nome = str(input('Qual seu nome ? '))
if nome == 'Henrique':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
