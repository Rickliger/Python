def notas(*n, sit=False):
    """
    -> Analisa notas e situações de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao indicar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    r = dict()
    r['total'] = list(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(10, 5, 7.5, 6.2, 4.6, 8.2, sit=True)
print(resp)

help(notas)