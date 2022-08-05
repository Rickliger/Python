tabela = (
          'PAL', 'ATP', 'ATM', 'COR', 'INT',
          'FLU', 'SPF', 'FLA', 'SAN', 'BOT',
          'AVA', 'COR', 'AMG', 'BRG', 'CEA',
          'ATG', 'GOI', 'CUI', 'FTL', 'JUV')

print(f'5 primeiros {tabela[0:5]}')

print('*'*20)
print(f'4 ultimos {tabela[-4:]}')
print('*'*20)

print(f'{sorted(tabela)}')

print('*'*20)

print(f'O internacional esta na {tabela.index("INT")} ª posição')
