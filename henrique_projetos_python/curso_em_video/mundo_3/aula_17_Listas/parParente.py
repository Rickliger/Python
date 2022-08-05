"""c = 0
r = ''
pe = pd = 0
while True:
    expre = str(input('Digite a expressão: '))
    pe = expre.count('(')
    pd = expre.count(')')
    #print(pd, pe)
    if pd == pe:
        print('Sua expressão é válida.')
    else:
        print('Sua expressão é inválida.')
    r = str(input('Quer continuar ? '))
    if r in 'Nn':
        break
print('Fim do programa')"""
expre = str(input('Digite a expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
