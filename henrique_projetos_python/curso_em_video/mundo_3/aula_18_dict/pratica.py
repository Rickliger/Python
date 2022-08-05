"""pessoas = {'nome': 'Henrique', 'sexo': 'M', 'idade': 23}

pessoas['nome'] = 'Rafa'
pessoas['peso'] = 75.7
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print('Keys', k)
print()
for k in pessoas.values():
    print('Values', k)
print()
for k, v in pessoas.items():
    print('Items', f'{k}: {v}')
brasil = []
estado1 = {'UF': 'Rio Grande do Sul', 'Sigla': 'RS'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1, '\n', estado2)
print()
print(brasil[0]['UF'], end=': ')
print(brasil[0]['Sigla'])"""

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla do Estado? ')).upper()
    brasil.append(estado.copy())
print(brasil)
"""for e in brasil:
    #for k, v in e.items():
    for v in e.values():
        #print(f'O campo {k} tem valor {v}')
        print(v, end=': ')
    print()"""
