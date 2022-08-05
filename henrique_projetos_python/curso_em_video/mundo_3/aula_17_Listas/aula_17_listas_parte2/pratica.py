"""teste = list()
teste.append('Henrique')
teste.append(23)
galera = list()
galera.append(teste[:])
teste[0] = 'Rafael'
teste[1] = 22
galera.append(teste[:])
print(galera)"""
"""galera = [['Henrique', 23], ['Ana', 33], ['Joaquin', 12], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')"""
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é 18+')
        totmai += 1
    else:
        print(f'{p[0]} é 18-')
        totmen += 1

print(f'Na galera temos {totmai} 18+ e {totmen} 18-')

#for i in galera:
    #print(f'Nome:{i[0]}, {i[1]} anos')