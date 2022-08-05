aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] <= 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
