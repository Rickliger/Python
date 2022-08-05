man = mais18 = menos20fem = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [s/n]')).upper().strip()[0]
    if continuar == 'N':
        break
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        man += 1
    if sexo == 'F' and idade < 20:
        menos20fem += 1
print(f'''O total de 18+ foi {mais18}, 
de homens foi {man}, 
e de mulheres com 20- foi {menos20fem}''')
